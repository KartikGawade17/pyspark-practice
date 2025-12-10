import os
from pyspark.sql import SparkSession

PYTHON_PATH = r"C:\Users\Kartik\anaconda3\envs\myenv\python.exe"

os.environ["PYSPARK_PYTHON"] = PYTHON_PATH
os.environ["PYSPARK_DRIVER_PYTHON"] = PYTHON_PATH

def get_spark(app_name="MySparkApp"):
    return SparkSession.builder \
        .appName(app_name) \
        .master("local[*]") \
        .config("spark.executorEnv.PYSPARK_PYTHON", PYTHON_PATH) \
        .getOrCreate()
