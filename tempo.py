import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017')
db = client['cricket']
collection = db['Data1']

# Fetch data from MongoDB collection
data_from_db = list(collection.find())

# Create DataFrame
df = pd.DataFrame(data_from_db)

# Convert 'Year' column to datetime
df['date'] = pd.to_datetime(df['date'], format='%Y')

# Calculate temporal distribution by year
yearly_counts = df['date'].dt.year.value_counts().sort_index()

# Calculate average frequency
average_frequency = yearly_counts.mean()

# Plot bullet graph
plt.figure(figsize=(10, 6))

# Plot bars for actual frequency
plt.bar(yearly_counts.index, yearly_counts, color='skyblue')

# Plot reference line for average frequency
plt.axhline(y=average_frequency, color='gray', linestyle='--')

# Annotate the average frequency
plt.text(yearly_counts.index.min(), average_frequency, f'Average: {average_frequency:.2f}', va='bottom', ha='right', color='gray')

plt.title('Temporal Distribution of Events by Year')
plt.xlabel('Year')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()
