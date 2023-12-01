from graphframes import *
from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql import functions as f
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')
plt.style.use('fivethirtyeight')
spark = SparkSession()

nodes = spark.read.csv('../data/airports.csv', header=False)
cleaned_nodes = nodes.select('_c1', '_c3', '_c5', '_c6', '_c7').filter("_c3 = 'United States'").withColumnRenamed('_c1',
                                                                                                                  'name').withColumnRenamed(
    '_c4', 'id').withColumnRenamed('_c6', 'latitude').withColumnRenamed('_c7', 'longitude').drop('_c3')
cleaned_nodes = cleaned_nodes[cleaned_nodes['id'] != '\\N']
relationships = spark.read.csv('../data/sw-relationships.csv', header=True)
cleaned_relationships = relationships.select('ORIGIN', 'DEST', 'FL_DATE', 'DEP_DELAY', 'ARR_DELAY', 'DISTANCE',
                                             'TAIL_NUM', 'FL_NUM', 'CRS_DEP_TIME', 'CRS_ARR_TIME',
                                             'UNIQUE_CARRIER').withColumnRenamed('ORIGIN', 'src').withColumnRenamed(
    'DEST', 'dst').withColumnRenamed('DEP_DELAY', 'deptDelay').withColumnRenamed('ARR_DELAY',
                                                                                 'arrDelay').withColumnRenamed(
    'TAIL_NUM', 'tailNumber').withColumnRenamed('FL_NUM', 'flightNumber').withColumnRenamed('FL_DATE',
                                                                                            'data').withColumnRenamed(
    'CRS_DEP_TIME', 'time').withColumnRenamed('CRS_ARR_TIME', 'arrivalTime').withColumnRenamed('DISTANCE',
                                                                                               'distance').withColumnRenamed(
    'UNIQUE_CARRIER', 'airline').withColumn('deptDelay', f.col('deptDelay').cast(FloatType())).withColumn('arrDelay',
                                                                                                          f.col(
                                                                                                              'arrDelay').cast(
                                                                                                              FloatType())).withColumn(
    'time', f.col('time').cast(IntegerType())).withColumn('arrivalTime', f.col('arrivalTime').cast(IntegerType()))
