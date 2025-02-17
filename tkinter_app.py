from systemcommands import *
import tkinter as tk

value = ""

def insert_text(text_widget, text):
    text_widget.insert(tk.END, f"{text}\n")

def on_key_press(event):
    global value
    value += event.char
    insert_text(text_widget, f"Key pressed: {event.char}")

def main(name):
    global text_widget
    root = tk.Tk()
    root.title(name)
    label = tk.Label(root, text=f"Welcome to {name}!")
    label.pack()
    
    text_widget = tk.Text(root)
    text_widget.pack()
    
    root.bind('<Key>', on_key_press)

    root.geometry("400x300")
    return root, text_widget

if __name__ == "__main__":
    root, text_widget = main('My App')
    root.mainloop()
