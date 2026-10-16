from spark_session import get_spark

spark = get_spark("test")
df = spark.createDataFrame([(1, "Alice"), (2, "Bob")], ["id", "name"])
df.show()
spark.stop()