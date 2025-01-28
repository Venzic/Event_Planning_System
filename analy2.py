import pandas as pd
import matplotlib.pyplot as plt
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017')
db = client['cricket']
collection = db['Data1']

# Fetch data from MongoDB collection
data_from_db = list(collection.find())

# Create DataFrame
df = pd.DataFrame(data_from_db)

# Convert budget to lakhs
df['budget_lakhs'] = df['budget'] / 1e5

# Budget Distribution Analysis - Pie Chart
plt.figure(figsize=(10, 6))

# Calculate frequencies for each budget range
hist, bins = pd.cut(df['budget_lakhs'], bins=10).value_counts(sort=False, normalize=True).values, pd.cut(df['budget_lakhs'], bins=10).value_counts(sort=False, normalize=True).index

# Plot pie chart
plt.pie(hist, labels=[f'{int(b.left)}L-{int(b.right)}L' for b in bins], autopct='%1.1f%%', startangle=140, colors=plt.cm.tab10.colors)
plt.title('Budget Distribution', fontsize=16)

plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.tight_layout()
plt.show()
