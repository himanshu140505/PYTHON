import os
import sys
from datetime import datetime, timedelta
from systemcommands import *
from tkinter_app import TkinterApp

class ALARM_CLOCK:
    def __init__(self, app):
        self.app = app

    def set_alarm(self, time_str):
        try:
            alarm_time = datetime.strptime(time_str, "%H:%M").time()
            current_time = datetime.now().time()
            if alarm_time > current_time:
                delta = datetime.combine(datetime.today(), alarm_time) - datetime.combine(datetime.today(), current_time)
            else:
                delta = datetime.combine(datetime.today() + timedelta(days=1), alarm_time) - datetime.combine(datetime.today(), current_time)
            self.app.root.after(int(delta.total_seconds() * 1000), self.trigger_alarm)
        except ValueError:
            self.app.insert_text("Invalid time format. Please use HH:MM.")

    def trigger_alarm(self):
        self.app.insert_text("Alarm! Time to wake up!")
        # Add any additional alarm actions here, such as playing a sound

    def start(self):
        self.app.run()

if __name__ == "__main__":
    app = TkinterApp('Alarm Clock')
    alarm_clock = ALARM_CLOCK(app)
    app.create_box(width=20, bd=2, relief="sunken")
    app.input_box.bind('<Return>', lambda event: alarm_clock.set_alarm(app.input_box.get()))
    alarm_clock.start()