import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import subprocess


class AnalysisPage(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Analysis Page")
        self.attributes('-fullscreen', True)  # Set fullscreen mode

        # Create a style for buttons
        self.style = ttk.Style()
        self.style.configure("Analyze.TButton", font=("Helvetica", 12, "bold"))
        self.style.map("Analyze.TButton", foreground=[("active", "white"), ("pressed", "white")])

        # Create a notebook to contain multiple pages
        self.notebook = ttk.Notebook(self)

        # Create five sections with titles, descriptions, images, and dropdown lists
        sections = [
            {"title": "Frequency of Food Types", "description": "Analyzing the frequency of food types involves examining the distribution of different types of food items.", "image_path": r"C:\Users\Venzic Barbosa\Desktop\Project Pics\11.jpg", "script": "anal.py"},
            {"title": "Venue Utilization", "description": "Analyzing venue utilization involves studying the usage of different stadiums for events.", "image_path": r"C:\Users\Venzic Barbosa\Desktop\Project Pics\7.jpg", "script": "venue.py"},
            {"title": "Budget Distribution", "description": "Analyzing budget distribution involves studying the allocation of funds across different categories.", "image_path": r"C:\Users\Venzic Barbosa\Desktop\Project Pics\8.jpg", "script": "analy2.py"},
            {"title": "Frequency of Events by State", "description": "Analyzing the frequency of events by state involves examining the distribution of events across various states.", "image_path": r"C:\Users\Venzic Barbosa\Desktop\Project Pics\5.jpg", "script": "geog.py"},
            {"title": "Temporal Distribution of Events", "description": "Analyzing the temporal distribution of events involves studying the timing and frequency of events over time.", "image_path": r"C:\Users\Venzic Barbosa\Desktop\Project Pics\4.jpg", "script": "tempo.py"},
        ]

        for section in sections:
            frame = ttk.Frame(self.notebook)
            self.create_section(frame, section)
            self.notebook.add(frame, text=section["title"])

        self.notebook.pack(expand=1, fill="both")

        # Add an exit button
        exit_button = tk.Button(self, text="Exit", command=self.quit, font=("Helvetica", 12, "bold"), bg="red", fg="white")
        exit_button.place(relx=0.95, rely=0.05, anchor="center")

    def create_section(self, frame, section):
        # Add title label
        title_label = ttk.Label(frame, text=section["title"], font=("Helvetica", 16, "bold"))
        title_label.pack(pady=(10, 0))

        # Add description label
        description_label = ttk.Label(frame, text=section["description"], wraplength=500, padding=(10, 10))
        description_label.pack()

        # Get screen dimensions
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Add Canvas for the background image
        canvas = tk.Canvas(frame, width=screen_width, height=screen_height)
        canvas.pack(fill=tk.BOTH, expand=True)  # Fill the entire frame

        # Add image as background
        if "image_path" in section:
            image = Image.open(section["image_path"])
            # Resize the image to fit the screen
            image = image.resize((screen_width, screen_height), Image.LANCZOS)
            section["photo_image"] = ImageTk.PhotoImage(image)
            canvas.create_image(0, 0, anchor=tk.NW, image=section["photo_image"])

        # Create a frame for buttons
        button_frame = ttk.Frame(canvas)
        button_frame.pack(pady=10)

        # Add Analyze button
        analyze_button = ttk.Button(button_frame, text="Analyze", command=lambda: self.show_specific_page(section["script"]), style="Analyze.TButton")
        analyze_button.pack(side=tk.LEFT, padx=20)

        # Add back button
        back_button = ttk.Button(button_frame, text="Back to Login", command=self.go_to_login, style="Analyze.TButton")
        back_button.pack(side=tk.LEFT)

    def show_specific_page(self, script_name):
        # Launch the specified script as a separate process
        subprocess.Popen(["python", script_name])

    def go_to_login(self):
        # Open login.py file as a separate process
        subprocess.Popen(["python", "login.py"])

if __name__ == "__main__":
    app = AnalysisPage()
    app.mainloop()
