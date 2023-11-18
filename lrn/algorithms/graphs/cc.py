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