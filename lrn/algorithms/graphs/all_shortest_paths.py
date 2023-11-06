from graphframes import *
from pyspark.sql import SparkSession

spark = SparkSession()
v = spark.read.csv('data/transport-nodes.csv', header=True)
e = spark.read.csv('data/transport-relationships.csv', header=True)
g = GraphFrame(v, e)
result = g.shortestPaths(['Colchester', 'Immingham', 'Hoek van Holland'])
result.sort(['id']).select('id', 'distances').show(truncate=False)
