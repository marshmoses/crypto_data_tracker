
# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pymysql

# Function to fetch data from MySQL
def fetch_data_from_mysql(query):
    try:
        # Establish a connection to the MySQL database
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='Newpassword18702#',
            database='crypto_data'
        )

        # Fetch data using the provided query
        df = pd.read_sql(query, connection)

        # Close the database connection
        connection.close()

        return df

    except Exception as e:
        print(f"Error fetching data from MySQL: {e}")
        return None

# Example query to fetch data from MySQL
mysql_query = "SELECT * FROM your_table_name"
df = fetch_data_from_mysql(mysql_query)

# Display basic information about the dataset
print("Dataset Information:")
print(df.info())

# Display the first few rows of the dataset
print("\nFirst Few Rows of the Dataset:")
print(df.head())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Perform data cleaning and preprocessing as needed

# Data Visualization

# Example: Histogram of a numerical column
plt.figure(figsize=(10, 6))
sns.histplot(df['numerical_column'], bins=20, kde=True)
plt.title('Histogram of Numerical Column')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.show()

# Example: Box plot for categorical vs numerical column
plt.figure(figsize=(12, 8))
sns.boxplot(x='categorical_column', y='numerical_column', data=df)
plt.title('Box Plot of Categorical vs Numerical Column')
plt.show()

# Example: Pair plot for numerical columns
sns.pairplot(df[['numerical_col1', 'numerical_col2', 'numerical_col3']])
plt.suptitle('Pair Plot of Numerical Columns', y=1.02)
plt.show()

# Example: Correlation heatmap
correlation_matrix = df.corr()
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=.5)
plt.title('Correlation Heatmap')
plt.show()

# Example Business Questions:

# 1. What is the distribution of values in a specific numerical column?
# 2. How does a numerical variable vary across different categories in a categorical column?
# 3. Are there any correlations between numerical variables?
# 4. What is the overall trend or pattern in the dataset?
# 5. How many missing values are there in each column?

# Answer these questions using the visualizations and analysis performed above.

# Save the cleaned and preprocessed dataset if needed
# df.to_csv('cleaned_dataset.csv', index=False)
