from systemcommands import *
import tkinter as tk

class TkinterApp:
    def __init__(self, name):
        self.value = ""
        self.owner_text = owner_text()
        self.root = tk.Tk()
        self.root.title(name)
        
        self.label = tk.Label(self.root, text=f"{self.owner_text}")
        self.label.pack()
        
        self.text_widget = tk.Text(self.root, height=10, width=50)
        self.text_widget.pack(pady=10)

        self.create_box()

    def create_box(self, **kwargs):
        self.input_box = tk.Entry(self.root, **kwargs)
        self.input_box.pack()
        self.input_box.bind("<Return>", self.on_entry_return)
        return self.input_box

    def insert_text(self, text):
        self.text_widget.insert(tk.END, f"{text}\n")
        
    def on_key_press(self, event):
        self.value += event.char
        self.insert_text(f"Key pressed: {event.char}")
        
    def get_input(self):
        return self.value
    
    def on_entry_return(self, event):
        # self.insert_text(f"Entry content: {self.input_box.get()}")
        print(f"Entry content: {self.input_box.get()}")
        self.input_box.delete(0, tk.END)
    
    def clear_text(self, input_box=None):
        self.text_widget.delete('1.0', tk.END)
        self.input_box.destroy()
        if input_box:
            input_box.delete(0, tk.END)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = TkinterApp('My App')
    app.run()
