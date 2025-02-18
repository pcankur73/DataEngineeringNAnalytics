import pandas as pd
from sqlalchemy import create_engine

# Establish database connection
engine = create_engine('mysql+pymysql://user:password@localhost/dbname')

### 1. Load CSV into MySQL

def load_csv_to_mysql(file_path, table_name):
    df = pd.read_csv(file_path)
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)
    print(f"Data loaded into {table_name}")

### 2. Query MySQL Data into Pandas DataFrame

def query_mysql(query):
    df = pd.read_sql(query, con=engine)
    return df

### 3. Data Cleaning Before Inserting into MySQL

def clean_and_insert(df, table_name):
    df.dropna(inplace=True)
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)
    print(f"Cleaned data inserted into {table_name}")

### 4. Aggregating Sales Data

def aggregate_sales():
    query = "SELECT product_name, SUM(sales) AS total_sales FROM sales_data GROUP BY product_name"
    df = pd.read_sql(query, con=engine)
    return df

### 5. Analyzing Customer Churn

def customer_churn():
    query = """
    SELECT customer_id, MAX(transaction_date) AS last_purchase
    FROM transactions
    GROUP BY customer_id
    HAVING MAX(transaction_date) < DATE_SUB(NOW(), INTERVAL 6 MONTH)
    """
    df = pd.read_sql(query, con=engine)
    return df

### 6. Create and Populate a Table

def create_table_from_df(df, table_name):
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)
    print(f"Table {table_name} created and populated")

### 7. Convert Datetime Format

def convert_datetime(df, column):
    df[column] = pd.to_datetime(df[column], format='%Y-%m-%d')
    return df

### 8. Join Two MySQL Tables

def join_tables():
    df1 = pd.read_sql("SELECT * FROM orders", con=engine)
    df2 = pd.read_sql("SELECT * FROM customers", con=engine)
    merged_df = pd.merge(df1, df2, on="customer_id", how="inner")
    return merged_df

### 9. Compute Monthly Sales Trends

def monthly_sales_trends():
    query = "SELECT DATE_FORMAT(sale_date, '%Y-%m') AS month, SUM(amount) AS total FROM sales GROUP BY month"
    df = pd.read_sql(query, con=engine)
    return df

### 10. Save Pandas DataFrame as MySQL Table with Auto-Increment ID

def save_with_auto_increment(df, table_name):
    from sqlalchemy import Integer
    df.to_sql(table_name, con=engine, if_exists='replace', index=False, dtype={'id': Integer})
    print(f"Table {table_name} saved with auto-increment ID")

### 11. Fetch Large MySQL Data Using Chunks

def fetch_large_data():
    chunks = pd.read_sql("SELECT * FROM large_table", con=engine, chunksize=10000)
    for chunk in chunks:
        print(chunk.head())

### 12. Identify Duplicate Entries

def find_duplicates():
    df = pd.read_sql("SELECT * FROM sales", con=engine)
    duplicates = df[df.duplicated()]
    return duplicates

### 13. Perform MySQL Update with Pandas

def update_mysql_data():
    update_query = "UPDATE employees SET salary = salary * 1.05 WHERE performance = 'Excellent'"
    engine.execute(update_query)

### 14. Find Top 5 Most Purchased Products

def top_products():
    query = "SELECT product_name, COUNT(*) AS count FROM sales GROUP BY product_name ORDER BY count DESC LIMIT 5"
    df = pd.read_sql(query, con=engine)
    return df

### 15. Detect Outliers in Sales Data

def detect_outliers():
    df = pd.read_sql("SELECT * FROM sales", con=engine)
    df['zscore'] = (df['amount'] - df['amount'].mean()) / df['amount'].std()
    outliers = df[df['zscore'].abs() > 3]
    return outliers

### 16. Fetch and Save MySQL Query Results as CSV

def save_query_to_csv(query, file_path):
    df = pd.read_sql(query, con=engine)
    df.to_csv(file_path, index=False)
    print(f"Query results saved to {file_path}")

### 17. Create a Pivot Table from MySQL Data

def pivot_table():
    df = pd.read_sql("SELECT * FROM sales", con=engine)
    pivot = df.pivot_table(index="product_name", columns="region", values="sales", aggfunc="sum")
    return pivot

### 18. Count Unique Customers per Month

def unique_customers_per_month():
    query = """
    SELECT DATE_FORMAT(transaction_date, '%Y-%m') AS month, COUNT(DISTINCT customer_id) AS unique_customers
    FROM transactions GROUP BY month
    """
    df = pd.read_sql(query, con=engine)
    return df

### 19. Group Sales Data by Product Category

def group_sales_by_category():
    query = "SELECT category, SUM(sales) AS total_sales FROM sales GROUP BY category"
    df = pd.read_sql(query, con=engine)
    return df

### 20. Convert MySQL Data to JSON

def convert_mysql_to_json():
    df = pd.read_sql("SELECT * FROM customers", con=engine)
    json_data = df.to_json(orient="records")
    return json_data
