from pyspark.sql import SparkSession
from graphframes import *

spark = SparkSession()
v = spark.read.csv('data/social-nodes.csv', header=True)
e = spark.read.csv('data/social-relationships.csv', header=True)
g = GraphFrame(v, e)
results = g.pageRank(resetProbability=0.15, maxIter=20)
results.vertices.sort('pagerank', ascending=False).show()
results = g.pageRank(resetProbability=0.15, tol=0.01)
results.vertices.sort('pagerank', ascending=False).show()
me = 'Doug'
results = g.pageRank(resetProbability=0.15, maxIter=20, sourceId=me)
people_to_follow = results.vertices.sort('pagerank', ascending=False)
already_to_follows = list(g.edges.filter(f"src='{me}'").toPandas()['dst'])
people_to_exclude = already_to_follows + [me]
people_to_follow[~people_to_follow.id.isin(people_to_exclude)].show()
