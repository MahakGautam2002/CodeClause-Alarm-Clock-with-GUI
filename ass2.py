import datetime
import tkinter as tk
from tkinter import messagebox
from playsound import playsound

class AlarmClock:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x350")
        self.root.title("Alarm Clock")

        self.time_label = tk.Label(self.root, font=("Helvetica", 35))
        self.time_label.pack(pady=20)

        self.alarm_time_var = tk.StringVar(value="HH:MM")
        self.alarm_entry = tk.Entry(self.root, textvariable=self.alarm_time_var)
        self.alarm_entry.pack(pady=10)

        self.set_button = tk.Button(self.root, text="Set Alarm", command=self.set_alarm)
        self.set_button.pack(pady=10)

        self.quit_button = tk.Button(self.root, text="Quit", command=self.quit)
        self.quit_button.pack(pady=10)

        self.alarm_is_set = False
        self.update_clock()

        self.root.mainloop()

    def update_clock(self):
        now = datetime.datetime.now()
        self.time_label.config(text="Current Time:"+now.strftime("%H:%M:%S"))
        if self.alarm_is_set and now.strftime("%H:%M") == self.alarm_time_var.get():
            self.alarm()
        self.root.after(1000, self.update_clock)

    def set_alarm(self):
        self.alarm_is_set = True

    def alarm(self):
        self.alarm_is_set = False
        self.alarm_time_var.set("")
        playsound("tone.mp3")
        messagebox.showinfo("Alarm", "Time to wake up!")
        

    def quit(self):
        self.root.destroy()

if __name__ == "__main__":
    alarm_clock = AlarmClock()
