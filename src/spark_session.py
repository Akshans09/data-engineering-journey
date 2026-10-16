import os
import sys
from pyspark.sql import SparkSession


def get_spark(app_name="app"):
    os.environ["PYSPARK_PYTHON"] = sys.executable
    os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable
    return SparkSession.builder.master("local[*]").appName(app_name).getOrCreate()