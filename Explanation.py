Explanation:
1️⃣ Installing PySpark
pip install pyspark
This installs PySpark, a tool that helps us process large amounts of data efficiently.
If you're using Google Colab, you might need to restart the runtime after installing it.
2️⃣ Importing Spark
from pyspark.sql import SparkSession
We need SparkSession to interact with Spark.
Think of it as a control center for managing data.
3️⃣ Starting a Spark Session
spark = SparkSession.builder.appName("HolidifyAnalysis").getOrCreate()
This creates a new Spark session or retrieves an existing one.
We name our session "HolidifyAnalysis" (this can be anything you like).
Without this, we can’t use PySpark DataFrames.
4️⃣ Loading the Dataset
file_path = "/content/holidify (1).csv"  
df = spark.read.csv(file_path, header=True, inferSchema=True)
We’re loading a CSV file from the given location.
header=True tells Spark that the first row contains column names.
inferSchema=True automatically figures out the type of data (numbers, text, etc.).
5️⃣ Checking the Data
df.printSchema()
df.show(5)
printSchema() → Displays the column names and their data types.
show(5) → Shows the first 5 rows of our dataset.
💡 Why? → This helps us understand the structure of our data.
6️⃣ Counting the Rows
print(f"Total Rows: {df.count()}")
This simply counts the total number of rows in the dataset.
Useful for knowing how big our data is.
7️⃣ Getting Summary Statistics
df.describe().show()
This gives basic statistics for each numeric column (like rating or price if they exist).
It shows things like:
Average (mean)
Minimum & Maximum
Standard deviation (how spread out the values are)
💡 Why? → This helps us understand the overall distribution of the data.
8️⃣ Finding the Most Popular Cities
df.groupBy("City").count().orderBy("count", ascending=False).show(10)
We’re grouping the data by city and counting how many times each city appears.
Then we sort it in descending order to see which cities are the most popular.
Finally, we show the top 10 cities.
💡 Why? → This helps us identify the most frequently mentioned cities in the dataset.
9️⃣ Filtering Highly Rated Places
df.filter(df["rating"] > 4.5).show(10)
We’re selecting only the places that have a rating greater than 4.5.
show(10) → Displays the first 10 results.
 This helps us quickly find the best-rated destinations.

