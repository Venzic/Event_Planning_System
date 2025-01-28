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

# Geographical Analysis
state_counts = df['state'].value_counts()

# Plot
plt.figure(figsize=(8, 5))
state_counts.plot(kind='bar', color='orange')
plt.title('Frequency of Events by State')
plt.xlabel('State')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()