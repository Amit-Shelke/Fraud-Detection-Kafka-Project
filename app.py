import findspark
findspark.init()

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("FraudDetection") \
    .getOrCreate()

print("Spark session started:", spark)
