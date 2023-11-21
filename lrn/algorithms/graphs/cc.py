from pyspark.sql.types import *
from graphframes import *

from graphframes.lib import AggregateMessages as AM
from pyspark.sql import functions as F
from operator import itemgetter


def collect_paths(paths):
    return F.collect_set(paths)


collect_paths_udf = F.udf(collect_paths, ArrayType(StringType()))
paths_type = ArrayType(StructType([StructField('id', StringType()), StructField('distance', IntegerType())]))


def flatten(ids):
    flat_list = [item for sublist in ids for item in sublist]
    return list(dict(sorted(flat_list, key=itemgetter(0))).items())


flatten_udf = F.udf(flatten, paths_type)


def new_paths(paths, id):
    paths = [{'id': col1, 'distance': col2 + 1} for col1, col2 in paths if col1 != id]
    paths.append({'id': id, 'distance': 1})
    return paths


new_paths_udf = F.udf(new_paths, paths_type)


def merge_paths(ids, new_ids, _id):
    joined_ids = ids + (new_ids if new_ids else [])
    merged_ids = [(col1, col2) for col1, col2 in joined_ids if col1 != _id]
    best_ids = dict(sorted(merged_ids, key=itemgetter(1), reverse=True))
    return [{'id': col1, 'distance': col2} for col1, col2 in best_ids.items()]


merge_paths_udf = F.udf(merge_paths, paths_type)


def calculate_closeness(ids):
    nodes = len(ids)
    total_distance = sum([col2 for _, col2 in ids])
    return 0 if total_distance == 0 else nodes * 1.0 / total_distance


closeness_udf = F.udf(calculate_closeness, DoubleType())

vertices = g.vertices.withColumn('ids', F.array())
cached_vertices = AM.getCachedDataFrame(vertices)
g2 = GraphFrame(cached_vertices, g.edges)
