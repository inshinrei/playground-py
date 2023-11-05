def is_valid(img, row, col):
    return 0 <= row < len(img) and 0 <= col < len(img[0])


def neighbors(img, row, col, start):
    indices = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
    return [(row, col) for row, col in indices if is_valid(img, row, col) and img[row][col] == start]


def flood_fill(img, row, col, p):
    start = img[row][col]
    queue = [(row, col)]
    visited = set()
    while len(queue) > 0:
        row, col = queue.pop(0)
        visited.add((row, col))
        img[row][col] = p
        for row, col in neighbors(img, row, col, start):
            if (row, col) not in visited:
                queue.append((row, col))
    return img


from graphframes import *
from pyspark.sql.types import *
from pyspark.sql import SparkSession
import pandas as pd

spark = SparkSession()

fields = [
    StructField('id', StringType(), True),
    StructField('latitude', FloatType(), True),
    StructField('longitude', FloatType(), True),
    StructField('population', IntegerType(), True)
]
v = spark.read.csv('data/transport-nodes.csv', header=True, schema=StructType(fields))
src_dst = spark.read.csv('data/transport-relationships.csv', header=True)
df_src_dst = src_dst.toPandas()
df_dst_src = src_dst.toPandas()
df_dst_src.columns = ['dst', 'src', 'relationship', 'cost']
e = spark.createDataFrame(pd.concat([df_src_dst, df_dst_src]))
g = GraphFrame(v, e)
(g.vertices.filter('population > 100000 and population < 300000').sort('population').show())
from_expr = "id='Den Haag'"
to_expr = "population > 100000 and population < 300000 and id <> 'Den Haag'"
result = g.bfs(from_expr, to_expr)
columns = [column for column in result.columns if not column.startswith('e')]
result.select(columns).show()
