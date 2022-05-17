from tkinter import *
from datetime import date

root = Tk()
root.title("Countdown to FREEDOM")
root.geometry("500x350")

title = Label(root, text="Complete masters in...", font=("Helvetica", 40), bg="#984ea3", fg="aquamarine")
title.pack(pady=20, ipadx=10, ipady=10)

# Get date
today = date.today()

# Format date
f_today = today.strftime("%A - %B %d, %Y")

# Displaying date
today_label = Label(root, text=f"Today is {f_today}")
today_label.pack(pady=20)

# Todays day in numbers
todays_day_num = int(today.strftime("%j"))

# Designated day
target_date = 266
days_left = target_date - todays_day_num

# Display days left
countdown_label = Label(root, text=f"There are only {days_left} days left until FREEDOM", font=("Helvetica", 15))
countdown_label.pack(pady=20)

root.mainloop()