from config.spark_init import get_spark

spark = get_spark("first_spark_app")

spark_data = spark.read.csv('temp.csv', header=True, inferSchema=True)

print(spark_data.head(3))