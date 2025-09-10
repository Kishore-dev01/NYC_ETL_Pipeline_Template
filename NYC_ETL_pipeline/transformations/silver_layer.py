import dlt
from pyspark.sql.functions import col

# Silver Layer: Cleaned and enriched data
@dlt.table(
  name="silver_nyc_taxi_data",
  comment="This is the cleaned and enriched NYC taxi data"
)
def silver_nyc_taxi_data():
    return (
        dlt.read("bronze_nyc_taxi_data")
        .select(
            col("LocationID").alias("location_id"),
            col("Borough").alias("borough"),
            col("Zone").alias("zone"),
            col("service_zone").alias("service_zone")
        )
        .filter(col("borough").isNotNull())
    )