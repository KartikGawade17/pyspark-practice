from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('dataframe_practise').getOrCreate()

#Read the dataset
dataset = spark.read.csv('temp.csv',header=True, inferSchema=True)
dataset.show()

# printSchema() is similar to pandas dataset.info() were we can see the datatype of the specific column.
dataset.printSchema()

# because when we ran the csv file in dataset we did not add inferschema because of that
# every data column it shows as string column. IMP = inferSchema=True

print(dataset.columns)


