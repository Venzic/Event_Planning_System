import pandas as pd
import matplotlib.pyplot as plt
from pymongo import MongoClient


# Title Popular Foods

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017')
db = client['cricket']
collection = db['Data1']

# Fetch data from MongoDB collection
data_from_db = list(collection.find())

# Create DataFrame
df = pd.DataFrame(data_from_db)

# Print column names
print(df.columns)

# Frequency Analysis of Food Types
food_type_counts = df['food_type'].value_counts()

# Plot
plt.figure(figsize=(8, 5))
food_type_counts.plot(kind='bar', color='skyblue')
plt.title('Frequency of Food Types')
plt.xlabel('Food Type')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
