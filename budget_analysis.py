import tkinter as tk
from tkinter import ttk
from pymongo import MongoClient
import pandas as pd

class BudgetAnalysisApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Budget Analysis")
        self.geometry("400x300")

        # Connect to MongoDB
        self.client = MongoClient('mongodb://localhost:27017')
        self.db = self.client['cricket']
        self.collection = self.db['Data1']

        # Create UI elements
        self.create_widgets()

    def create_widgets(self):
        # Label and dropdown for state selection
        self.state_label = ttk.Label(self, text="Select State:")
        self.state_label.pack()
        self.state_var = tk.StringVar()
        self.state_dropdown = ttk.Combobox(self, textvariable=self.state_var, values=self.get_states())
        self.state_dropdown.pack()

        # Label and dropdown for event selection
        self.event_label = ttk.Label(self, text="Select Event:")
        self.event_label.pack()
        self.event_var = tk.StringVar()
        self.event_dropdown = ttk.Combobox(self, textvariable=self.event_var, values=self.get_events())
        self.event_dropdown.pack()

        # Label and dropdown for venue selection
        self.venue_label = ttk.Label(self, text="Select Venue:")
        self.venue_label.pack()
        self.venue_var = tk.StringVar()
        self.venue_dropdown = ttk.Combobox(self, textvariable=self.venue_var, values=self.get_venues())
        self.venue_dropdown.pack()

        # Button to analyze budget
        self.analyze_button = ttk.Button(self, text="Analyze Budget", command=self.analyze_budget)
        self.analyze_button.pack()

    def get_states(self):
        # Query distinct states from MongoDB collection
        states = self.collection.distinct("state")
        return states

    def get_events(self):
        # Query distinct events from MongoDB collection
        events = self.collection.distinct("event")
        return events

    def get_venues(self):
        # Query distinct venues from MongoDB collection
        venues = self.collection.distinct("venue")
        return venues

    def analyze_budget(self):
        # Get user inputs
        state = self.state_var.get()
        event = self.event_var.get()
        venue = self.venue_var.get()

        # Query MongoDB collection based on user inputs
        query = {"state": state, "event": event, "venue": venue}
        data = self.collection.find(query)

        # Create DataFrame from query results
        df = pd.DataFrame(list(data))

        # Calculate average budget
        average_budget = df['budget'].mean()

        # Display result to user
        result_text = f"Estimated Budget: {average_budget:.2f} Lakhs"
        result_label = ttk.Label(self, text=result_text)
        result_label.pack()

if __name__ == "__main__":
    app = BudgetAnalysisApp()
    app.mainloop()
