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
