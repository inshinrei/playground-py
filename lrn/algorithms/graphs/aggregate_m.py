from pyspark.sql import SparkSession, DataFrame, functions as f
from pyspark import SparkContext


def _java_api(jsc):
    java_class_name = 'org.graphframes.GraphFramePythonAPI'
    return jsc._jvm.Thread.currentThread().getContextClassLoader().loadClass(java_class_name).newInstance()


class _Class_Property(object):
    def __init__(self, _f):
        self.f = _f
        self.__doc__ = _f.__doc__

    def __get__(self, _, owner):
        return self.f(owner)


class AggregateMessages(object):
    @_Class_Property
    def src(_):
        jvm_gf_api = _java_api(SparkContext)
        return f.col(jvm_gf_api.SRC())

    @_Class_Property
    def dst(_):
        jvm_gf_api = _java_api(SparkContext)
        return f.col(jvm_gf_api.DST())

    @_Class_Property
    def edge(_):
        jvm_gf_api = _java_api(SparkContext)
        return f.col(jvm_gf_api.EDGE())

    @_Class_Property
    def msg(_):
        jvm_gf_api = _java_api(SparkContext)
        return f.col(jvm_gf_api.aggregateMessages().MSG_COL_NAME())

    @staticmethod
    def getCachedDataFrame(df):
        sql_context = df.sql_ctx
        jvm_gf_api = _java_api(sql_context._sc)
        jdf = jvm_gf_api.aggregateMessages().getCachedDataFrame(df._jdf)
        return DataFrame(jdf, sql_context)
