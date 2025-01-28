import csv
import random
from datetime import datetime

states = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"]
events = ["Wedding", "Birthday", "Conference", "Engagement", "Baptism", "Orientation", "Housewarming", "First Holy Communion"]
venues = ["Indoor", "Outdoor", "Both"]
times = ["Morning", "Afternoon", "Evening"]
food_types = ["", "Vegetarian", "Non-vegetarian", "Specific"]
specific_food_styles = ["North Indian", "South Indian", "Goan", "Kerala Style", "North-East Style"]

# Function to generate random year between 2017 and 2019
def random_year():
    return random.randint(2010, 2019)

# Open CSV file for writing
with open('event_data.csv', 'w', newline='') as csvfile:
    fieldnames = ['_id', 'state', 'event', 'venue', 'Year', 'time', 'food_type', 'food', 'budget']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    for i in range(10000):
        _id = f"{i+1:08x}"
        state = random.choice(states)
        event = random.choice(events)
        venue = random.choice(venues)
        year = random_year()  # Generate random year
        time = random.choice(times)
        food_type = random.choice(food_types)
        specific_food_style = random.choice(specific_food_styles) if food_type == "Specific" else ""
        budget = random.randint(50000, 2000000)

        # Write row to CSV file
        writer.writerow({'_id': _id, 'state': state, 'event': event, 'venue': venue, 'Year': year, 'time': time, 'food_type': food_type, 'food': specific_food_style, 'budget': budget})

print("Data generated and saved to event_data.csv")
