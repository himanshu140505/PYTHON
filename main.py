import tkinter as tk
from tkinter import ttk, messagebox
import time
import ttkbootstrap as tb  # Optional: Provides modern UI themes


# ===========================
# 🔹 CLASS: Main Application
# ===========================
class AdvancedTkinterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Tkinter App")
        self.root.geometry("600x400")
        
        # 🌙 Default Theme: Light Mode
        self.current_theme = "light"

        # ===========================
        # 🔹 SECTION 1: MENU BAR
        # ===========================
        self.create_menu_bar()

        # ===========================
        # 🔹 SECTION 2: MAIN LAYOUT
        # ===========================
        self.create_tabs()

        # ===========================
        # 🔹 SECTION 3: CLOCK (Live Time)
        # ===========================
        self.clock_label = ttk.Label(self.root, font=("Arial", 12), foreground="blue")
        self.clock_label.pack(pady=5)
        self.update_clock()  # Start clock update loop


    # ===========================
    # 🔹 FUNCTION: OPEN NEW FILE WINDOW
    # ===========================
    def new_file(self):
        new_window = tk.Toplevel(self.root)  # Create a new window
        new_window.title("New Window")
        new_window.geometry("400x300")  # Set window size
        tk.Label(new_window, text="This is a new window", font=("Arial", 14)).pack(pady=20)


    # ===========================
    # 🔹 FUNCTION: MENU BAR
    # ===========================
    def create_menu_bar(self):
        menu_bar = tk.Menu(self.root)

        # File Menu
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file)  # Fixed reference to self.new_file
        file_menu.add_command(label="Open", command=lambda: print("Open File"))
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        # Help Menu
        help_menu = tk.Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)
        menu_bar.add_cascade(label="Help", menu=help_menu)

        self.root.config(menu=menu_bar)


    # ===========================
    # 🔹 FUNCTION: SHOW ABOUT INFO
    # ===========================
    def show_about(self):
        messagebox.showinfo("About", "Advanced Tkinter App v1.0\nCreated by You!")


    # ===========================
    # 🔹 FUNCTION: CREATE TABS
    # ===========================
    def create_tabs(self):
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill='both', expand=True)

        # 🟢 TAB 1: Input & Output
        tab1 = ttk.Frame(notebook)
        notebook.add(tab1, text="Home")
        self.create_input_output_tab(tab1)

        # 🟡 TAB 2: Theme Toggle
        tab2 = ttk.Frame(notebook)
        notebook.add(tab2, text="Settings")
        self.create_settings_tab(tab2)


    # ===========================
    # 🔹 FUNCTION: INPUT & OUTPUT UI
    # ===========================
    def create_input_output_tab(self, frame):
        label = ttk.Label(frame, text="Enter Something:", font=("Arial", 12))
        label.pack(pady=10)

        self.input_var = tk.StringVar()
        self.input_entry = ttk.Entry(frame, textvariable=self.input_var, font=("Arial", 12))
        self.input_entry.pack(pady=5)

        button = ttk.Button(frame, text="Submit", command=self.display_output)
        button.pack(pady=5)

        self.output_label = ttk.Label(frame, text="", font=("Arial", 12), foreground="green")
        self.output_label.pack(pady=10)


    # ===========================
    # 🔹 FUNCTION: SHOW OUTPUT
    # ===========================
    def display_output(self):
        user_text = self.input_var.get()
        if user_text:
            self.output_label.config(text=f"You Entered: {user_text}")
        else:
            messagebox.showwarning("Warning", "Please enter something!")
        return user_text
    

    # ===========================
    # 🔹 FUNCTION: SETTINGS TAB (THEME TOGGLE)
    # ===========================
    def create_settings_tab(self, frame):
        label = ttk.Label(frame, text="Toggle Theme:", font=("Arial", 12))
        label.pack(pady=10)

        theme_button = ttk.Button(frame, text="Switch Theme", command=self.toggle_theme)
        theme_button.pack(pady=5)


    # ===========================
    # 🔹 FUNCTION: TOGGLE DARK/LIGHT MODE
    # ===========================
    def toggle_theme(self):
        if self.current_theme == "light":
            self.root.tk_setPalette(background="#2e2e2e", foreground="white")
            self.current_theme = "dark"
        else:
            self.root.tk_setPalette(background="white", foreground="black")
            self.current_theme = "light"


    # ===========================
    # 🔹 FUNCTION: LIVE CLOCK
    # ===========================
    def update_clock(self):
        current_time = time.strftime("%H:%M:%S %p")
        self.clock_label.config(text=f"Current Time: {current_time}")
        self.root.after(1000, self.update_clock)  # Update every second



# ===========================
# 🔹 RUN THE APPLICATION
# ===========================
if __name__ == "__main__":
    root = tb.Window(themename="cosmo")  # Optional: ttkbootstrap theme
    app = AdvancedTkinterApp(root)
    root.mainloop()
