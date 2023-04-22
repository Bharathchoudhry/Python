import tkinter as tk
import calendar

class CalendarApp:
    def __init__(self, master):
        self.master = master
        self.master.title("12-Month Calendar")
        self.master.geometry("800x600")
        self.year_var = tk.IntVar()
        self.year_var.set(calendar.datetime.datetime.now().year)
        self.create_calendar()
    
    def create_calendar(self):
        year = self.year_var.get()
        calendar_frame = tk.Frame(self.master)
        calendar_frame.pack(side="top", padx=20, pady=20)
        for month in range(1, 13):
            month_frame = tk.Frame(calendar_frame)
            month_frame.pack(side="left", padx=10, pady=10)
            month_label = tk.Label(month_frame, text=calendar.month_name[month] + " " + str(year), font=("Arial", 18))
            month_label.pack(pady=10)
            month_cal_str = calendar.monthcalendar(year, month)
            for week in month_cal_str:
                week_str = ""
                for day in week:
                    if day == 0:
                        week_str += "   "
                    else:
                        week_str += " " + str(day) + " "
                week_label = tk.Label(month_frame, text=week_str)
                week_label.pack()
    
    def update_calendar(self):
        for widget in self.master.winfo_children():
            widget.destroy()
        self.create_calendar()

root = tk.Tk()
app = CalendarApp(root)
year_label = tk.Label(root, text="Enter year: ")
year_label.pack(side="left", padx=10, pady=10)
year_entry = tk.Entry(root, textvariable=app.year_var)
year_entry.pack(side="left", padx=10, pady=10)
update_button = tk.Button(root, text="Update Calendar", command=app.update_calendar)
update_button.pack(side="left", padx=10, pady=10)
root.mainloop()