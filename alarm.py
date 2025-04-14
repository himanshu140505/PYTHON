import pyglet
import time
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Alarm")
root.geometry("400x250")
root.configure(bg="#1e1e1e")  # Dark background

style = ttk.Style()
style.theme_use("default")

# Custom styles
style.configure("TFrame", background="#1e1e1e")
style.configure("TLabel", background="#1e1e1e", foreground="#ffffff", font=("Segoe UI", 14, "bold"))
style.configure("TEntry", font=("Segoe UI", 12), padding=5)
style.configure("TButton", font=("Segoe UI", 12), padding=6)

def Set():
    Alarm = entry.get()
    print("Alarm set for:", Alarm)
    Current = time.strftime("%H:%M")

    while Alarm != Current:
        Current = time.strftime("%H:%M")
        time.sleep(1)

    if Alarm == Current:
        song = pyglet.media.load('sound.mp3', streaming=False)
        player = pyglet.media.Player()
        player.queue(song)
        player.loop = True  # Loop the alarm sound
        player.play()
        pyglet.app.run()  # This keeps the sound loop running until the window is closed

frame = ttk.Frame(root)
frame.pack(pady=50)

label = ttk.Label(frame, text="⏰ Alarm Clock")
label.pack(pady=10)

entry = ttk.Entry(frame, width=30, justify="center")
entry.pack(pady=5)
entry.insert(3, "19:05")

button = ttk.Button(frame, text="Set Alarm", command=Set)
button.pack(pady=10)

root.mainloop()
