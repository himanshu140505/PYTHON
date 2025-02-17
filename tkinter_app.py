from systemcommands import *
import tkinter as tk

def insert_text(text_widget, text):
    text_widget.insert(tk.END, f"{text}\n")

def main(name):
    root = tk.Tk()
    root.title(name)
    label = tk.Label(root, text=f"Welcome to {name}!")
    label.pack()
    
    text = tk.Text(root)
    text.pack()
    
    root.geometry("400x300")
    return root, text

if __name__ == "__main__":
    root, text_widget = main('My App')
    root.mainloop()
