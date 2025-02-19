import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets
df_customers = pd.read_csv('/mnt/data/blinkit_extracted/blinkit_customers.csv')
df_orders = pd.read_csv('/mnt/data/blinkit_extracted/blinkit_orders.csv')
df_feedback = pd.read_csv('/mnt/data/blinkit_extracted/blinkit_customer_feedback.csv')
df_delivery = pd.read_csv('/mnt/data/blinkit_extracted/blinkit_delivery_performance.csv')
df_inventory = pd.read_csv('/mnt/data/blinkit_extracted/blinkit_inventory.csv')
df_marketing = pd.read_csv('/mnt/data/blinkit_extracted/blinkit_marketing_performance.csv')
df_order_items = pd.read_csv('/mnt/data/blinkit_extracted/blinkit_order_items.csv')
df_products = pd.read_csv('/mnt/data/blinkit_extracted/blinkit_products.csv')

# Case Study 1: Customer Segmentation Analysis
customer_segments = df_customers.groupby('customer_segment').agg({
    'total_orders': 'mean',
    'avg_order_value': 'mean'
}).reset_index()

plt.figure(figsize=(8, 5))
sns.barplot(x='customer_segment', y='total_orders', data=customer_segments)
plt.title("Average Orders by Customer Segment")
plt.show()

# Case Study 2: Delivery Performance Evaluation
delivery_performance = df_delivery.groupby('delivery_status').agg({
    'delivery_time_minutes': 'mean'
}).reset_index()

plt.figure(figsize=(8, 5))
sns.barplot(x='delivery_status', y='delivery_time_minutes', data=delivery_performance)
plt.title("Average Delivery Time by Status")
plt.show()

# Case Study 3: Marketing Campaign Effectiveness
marketing_performance = df_marketing.groupby('channel').agg({
    'roas': 'mean',
    'conversions': 'sum'
}).reset_index()

plt.figure(figsize=(8, 5))
sns.barplot(x='channel', y='roas', data=marketing_performance)
plt.title("ROAS by Marketing Channel")
plt.show()

# Case Study 4: Product Demand Forecasting
df_inventory['date'] = pd.to_datetime(df_inventory['date'], errors='coerce')
demand_trend = df_inventory.groupby(df_inventory['date'].dt.month)['stock_received'].sum()

demand_trend.plot(kind='line', figsize=(8, 5), marker='o', title="Product Demand Trend")
plt.show()

# Case Study 5: Sentiment Analysis of Customer Feedback
sentiment_counts = df_feedback['sentiment'].value_counts()

plt.figure(figsize=(8, 5))
sentiment_counts.plot(kind='bar', title="Customer Feedback Sentiment Analysis")
plt.show()

# Case Study 6: Revenue and Profitability Analysis
revenue_performance = df_orders.groupby(df_orders['order_date'].str[:7]).agg({
    'order_total': 'sum'
}).reset_index()

plt.figure(figsize=(8, 5))
plt.plot(revenue_performance['order_date'], revenue_performance['order_total'], marker='o')
plt.title("Monthly Revenue Trend")
plt.xticks(rotation=45)
plt.show()

# Case Study 7: Inventory Stock Optimization
inventory_status = df_inventory.groupby('product_id').agg({
    'stock_received': 'sum',
    'damaged_stock': 'sum'
}).reset_index()

plt.figure(figsize=(8, 5))
sns.scatterplot(x='stock_received', y='damaged_stock', data=inventory_status)
plt.title("Stock vs. Damaged Items")
plt.show()

# Case Study 8: Order Value and Payment Method Trends
payment_analysis = df_orders.groupby('payment_method').agg({
    'order_total': 'mean'
}).reset_index()

plt.figure(figsize=(8, 5))
sns.barplot(x='payment_method', y='order_total', data=payment_analysis)
plt.title("Average Order Value by Payment Method")
plt.show()

# Case Study 9: Geographical Sales Distribution
df_customers['area'] = df_customers['area'].fillna('Unknown')
location_sales = df_customers.groupby('area').agg({
    'total_orders': 'sum'
}).reset_index()

plt.figure(figsize=(10, 5))
sns.barplot(x='area', y='total_orders', data=location_sales)
plt.xticks(rotation=90)
plt.title("Sales Distribution by Area")
plt.show()

# Case Study 10: Customer Retention and Churn Prediction
df_customers['churn'] = df_customers['total_orders'].apply(lambda x: 1 if x == 0 else 0)
churn_rate = df_customers['churn'].mean() * 100
print(f"Customer Churn Rate: {churn_rate:.2f}%")

plt.figure(figsize=(8, 5))
sns.countplot(x=df_customers['churn'])
plt.title("Customer Churn Distribution")
plt.xticks([0, 1], ['Active', 'Churned'])
plt.show()
