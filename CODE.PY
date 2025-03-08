pip install pyspark
from pyspark.sql import SparkSession

# Initialize a Spark session
spark = SparkSession.builder.appName("HolidifyAnalysis").getOrCreate()

# Load the dataset
file_path = "/content/holidify (1).csv"  # Update this with your actual file path
df = spark.read.csv(file_path, header=True, inferSchema=True)

# Display schema and first few rows
df.printSchema()
df.show(5)
# Check number of rows
print(f"Total Rows: {df.count()}")

# Summary statistics
df.describe().show()
df.groupBy("City").count().orderBy("count", ascending=False).show(10)
# Changed "destination" to "City" as it's likely the correct column name
# Apply filter on the DataFrame 'df'
df.filter(df["rating"] > 4.5).show(10)
