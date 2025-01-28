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

# Venue Utilization Analysis
venue_counts = df['venue'].value_counts()

# Plot
plt.figure(figsize=(8, 5))

# Create donut pie chart
plt.pie(venue_counts, labels=venue_counts.index, autopct='%1.1f%%', startangle=90, colors=plt.cm.tab20.colors)
plt.title('Venue Utilization')

# Draw a circle at the center of pie to make it a donut
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.tight_layout()
plt.show()
