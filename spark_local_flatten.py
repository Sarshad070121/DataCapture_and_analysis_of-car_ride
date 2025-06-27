import os
import sys
os.environ["PYSPARK_PYTHON"] = "/opt/cloudera/parcels/Anaconda/bin/python"
os.environ["JAVA_HOME"] = "/usr/java/jdk1.8.0_161/jre"
os.environ["SPARK_HOME"] = "/opt/cloudera/parcels/SPARK2-2.3.0.cloudera2-1.cdh5.13.3.p0.316101/lib/spark2/"
os.environ["PYLIB"] = os.environ["SPARK_HOME"] + "/python/lib"
sys.path.insert(0, os.environ["PYLIB"] + "/py4j-0.10.6-src.zip")
sys.path.insert(0, os.environ["PYLIB"] + "/pyspark.zip")

from pyspark.sql import SparkSession
from pyspark.sql.functions import get_json_object

# Initialize Spark session
spark = SparkSession.builder.appName("Kafka-JSON-Flatten").getOrCreate()

# Read raw Kafka JSON output from HDFS
df = spark.read.json("/user/poushali/clickstream_json/part-*.json")

# Flatten the nested JSON structure using get_json_object
df = df.select(
    get_json_object(df['value_str'], "$.customer_id").alias("customer_id"),
    get_json_object(df['value_str'], "$.app_version").alias("app_version"),
    get_json_object(df['value_str'], "$.OS_version").alias("OS_version"),
    get_json_object(df['value_str'], "$.lat").alias("lat"),
    get_json_object(df['value_str'], "$.lon").alias("lon"),
    get_json_object(df['value_str'], "$.page_id").alias("page_id"),
    get_json_object(df['value_str'], "$.button_id").alias("button_id"),
    get_json_object(df['value_str'], "$.is_button_click").alias("is_button_click"),
    get_json_object(df['value_str'], "$.is_page_view").alias("is_page_view"),
    get_json_object(df['value_str'], "$.is_scroll_up").alias("is_scroll_up"),
    get_json_object(df['value_str'], "$.is_scroll_down").alias("is_scroll_down"),
    get_json_object(df['value_str'], "$.timestamp").alias("timestamp")
)

# Write the flattened DataFrame to HDFS in CSV format
df.coalesce(1).write.format("csv").mode("overwrite").option("header", "true").save("/user/poushali/clickstream_flattened")
