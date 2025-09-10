import dlt

# Bronze Layer: Raw data ingestion as a streaming table
@dlt.table(
  name="bronze_nyc_taxi_data",
  comment="This is the raw NYC taxi data"
)
def bronze_nyc_taxi_data():
    return (
        spark.read.format("csv")
        .option("header", "true")
        .load("dbfs:/databricks-datasets/nyctaxi/taxizone/taxi_zone_lookup.csv")
    )