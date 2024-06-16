import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")


root.config(bg="#ffffff")


lbl_time = tk.Label(root, text="", font=("CityLights Dots", 90, "bold"), bg="black",foreground="red")
lbl_time.pack(pady=10)


def update_time():
    now = strftime("%H:%M:%S %p")
    lbl_time.config(text=now)


    root.after(1000, update_time)


update_time()

root.mainloop()