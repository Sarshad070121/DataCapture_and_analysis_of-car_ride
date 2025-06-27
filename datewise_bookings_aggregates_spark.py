from pyspark.sql import SparkSession
from pyspark.sql.functions import from_unixtime, to_date, col

# Initialize Spark session
spark = SparkSession.builder.appName("DateWiseBookings").getOrCreate()

# Read parquet data
df = spark.read.parquet("hdfs:///user/poushali/rds_import/bookings")

# Extract date from timestamp and aggregate
df_with_date = df.withColumn("booking_date", to_date(from_unixtime(col("pickup_timestamp") / 1000)))
agg_df = df_with_date.groupBy("booking_date").count().withColumnRenamed("count", "total_bookings")

# Save it to HDFS directly
agg_df.coalesce(1).write.csv("hdfs:///user/poushali/datewise_bookings_output", header=True, mode="overwrite")