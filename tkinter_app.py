from systemcommands import *
import tkinter as tk

class TkinterApp:
    def __init__(self, name):
        self.root = tk.Tk()
        self.root.title(name)
        self.owner_text = owner_text()
        
        self.label = tk.Label(self.root, text=f"{self.owner_text}")
        self.label.pack()
        
        self.text_widget = tk.Text(self.root, height=10, width=50)
        self.text_widget.pack(pady=10)

    def create_box(self, **kwargs):
        self.input_box = tk.Entry(self.root, **kwargs)
        self.input_box.pack(pady=10)
        return self.input_box

    def insert_text(self, text):
        self.text_widget.insert(tk.END, f"{text}\n")
        
    def clear_text(self):
        self.text_widget.delete('1.0', tk.END)
        if hasattr(self, 'input_box'):
            self.input_box.delete(0, tk.END)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = TkinterApp('My App')
    app.run()
