 BIG-DATA-ANALYSIS

COMPANY NAME : CODTECH IT SOLUTIONS

NAME : SANJANA D

INTERN ID : CT08RDF

DOMAIN : DATA ANALYSIS

DURATION : 4 WEEKS

MENTOR : NEELA SANTHOSH KUMAR

EXPLANATION :
MY dataset contains 71 entries with five columns:
Id (Unique identifier for each entry)
City (Name of the travel destination)
Rating (A numerical rating for each city)
About the city (long Description) (A detailed description of the city)
Best Time to Visit (Recommended travel season)
The ratings range from 4.4 to 4.9, indicating that most cities in the dataset are highly rated.  ​​
The PySpark script is designed to analyze a dataset containing information about 71 travel destinations. It starts by installing and importing PySpark, then initializes a Spark session named "HolidifyAnalysis" to handle large-scale data processing efficiently.
The dataset is loaded from holidify (1).csv, where header=True ensures the first row is recognized as column names, and inferSchema=True allows Spark to determine data types automatically. The schema is printed to understand the structure, and the first five rows are displayed for an initial overview. The total number of rows is also counted, confirming that the dataset contains 71 entries.
To gain insights, the script generates summary statistics such as the minimum, maximum, and average values for numerical columns. The dataset includes a "City" column listing various travel destinations, a "Rating" column indicating how highly these cities are rated (ranging from 4.4 to 4.9), and details like the best time to visit and a long description of each location. The data is grouped by city, counting how frequently each city appears in the dataset, and the top 10 most mentioned cities are displayed.
Finally, the script applies a filter to highlight cities with a rating above 4.5, helping to identify the most highly rated travel destinations. With most cities already rated above 4.4, this step helps in focusing on the best-reviewed places, making it easier for travelers to choose top-rated destinations.








