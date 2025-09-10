import dlt

# Gold Layer: Aggregated and business-level data
@dlt.table(
  name="gold_nyc_taxi_data",
  comment="This is the aggregated NYC taxi data for business use"
)
def gold_nyc_taxi_data():
    return (
        dlt.read("silver_nyc_taxi_data")
        .groupBy("borough")
        .count()
        .alias("total_rides")
    )