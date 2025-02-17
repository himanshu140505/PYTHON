from systemcommands import *
import tkinter as tk
def insert_text(text_widget):
    text_widget.insert(tk.END, "I am the owner of this project")
def main(name):
    root = tk.Tk()
    root.title(name)
    label = tk.Label(root, text=f"Welcome to {name}!")
    text = tk.Text(root)
    insert_text(text)
    text.pack()
    label.pack()
    root.geometry("400x300")
    root.mainloop()
    

main('My App')