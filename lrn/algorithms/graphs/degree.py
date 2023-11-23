from pyspark.sql import SparkSession
from graphframes import *

spark = SparkSession()
v = spark.read.csv('data/social-nodes.csv', header=True)
e = spark.read.csv('data/social-relationships.csv', header=True)
g = GraphFrame(v, e)
total_degree = g.degrees
in_degree = g.inDegrees
out_degree = g.outDegrees
total_degree.join(in_degree, 'id', how='left').join(out_degree, 'id', how='left').fillna(0).sort('inDegree',
                                                                                                 ascending=False).show()
