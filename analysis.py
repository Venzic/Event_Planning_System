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
            {"title": "Popular Foods", "description": "Imagine a tantalizing array of culinary wonders, each one a beloved classic shrouded in mystery. There's an adventure waiting to unfold in the realm of popular foods. So why wait? Dive in and uncover the secrets that tantalize your taste buds, and let the delicious journey begin!", "image_path": r"C:\Users\Venzic Barbosa\Desktop\Project Pics\11.jpg"},
            {"title": "All States", "description": "Embark on an enchanting odyssey from the majestic landscapes of Kashmir to the sun-drenched shores of Kanyakumari, traversing the vibrant tapestry of India's diverse cultures along the way, ideal for your wedding celebration or cultural extravaganza.", "image_path": r"C:\Users\Venzic Barbosa\Desktop\Project Pics\7.jpg"},
            {"title": "Financial Estimate", "description": "Step into an experience where every expense is an investment in unforgettable memories. Our financial estimate guarantees the utmost value, ensuring every penny spent leads to a journey filled with unparalleled satisfaction and cherished moments that transcend monetary worth.", "image_path": r"C:\Users\Venzic Barbosa\Desktop\Project Pics\8.jpg"},
            {"title": "Chronicle Timeline", "description": "Step into the unfolding narrative of a chronological timeline, where each event is a chapter in the story of human history, guiding you through the evolution of civilizations and the remarkable achievements of mankind.", "image_path": r"C:\Users\Venzic Barbosa\Desktop\Project Pics\5.jpg"},
            {"title": "locus", "description": "Choosing the ideal venue is crucial, harmonizing budget, event needs, and popular preferences for a memorable and successful experience. We assist you in discovering a suitable and thoughtful plan to execute seamlessly.", "image_path": r"C:\Users\Venzic Barbosa\Desktop\Project Pics\4.jpg"},
            {"title": "Budget Analysis", "description": "Explore the distribution of budgets and analyze financial data to make informed decisions.", "image_path": r"C:\Users\Venzic Barbosa\Desktop\Project Pics\4.jpg"}
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
        analyze_button = ttk.Button(button_frame, text="Analyze", command=lambda: self.show_specific_page(section["title"]), style="Analyze.TButton")
        analyze_button.pack(side=tk.LEFT, padx=20)

        # Add back button
        back_button = ttk.Button(button_frame, text="Back to Login", command=self.go_to_login, style="Analyze.TButton")
        back_button.pack(side=tk.LEFT)

    def show_specific_page(self, section_title):
        try:
            if section_title == "Financial Estimate":
                # Launch budget_estimation.py as a separate process
                subprocess.Popen(["python", "analy2.py"])
            elif section_title == "Popular Foods":
                subprocess.Popen(["python", "anal.py"])
            elif section_title == "All States":
                subprocess.Popen(["python", "geog.py"])
            elif section_title == "Chronicle Timeline":
                subprocess.Popen(["python", "tempo.py"])
            elif section_title == "locus":
                subprocess.Popen(["python", "venue.py"])
            elif section_title == "Budget Analysis":
                subprocess.Popen(["python", "budget_analysis.py"])
            else:
                print(f"Button clicked for {section_title}")
        except Exception as e:
            print(f"Error occurred: {e}")

    def go_to_login(self):
        # Open login.py file as a separate process
        subprocess.Popen(["python", "login.py"])

if __name__ == "__main__":
    app = AnalysisPage()
    app.mainloop()
