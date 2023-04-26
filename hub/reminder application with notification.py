import time
import datetime
from playsound import playsound
import notify2

notify2.init('Reminder')

class Reminder:
    def __init__(self, name, date):
        self.name = name
        self.date = date

    def check_due_date(self):
        today = datetime.date.today()
        if self.date == today:
            return "due today"
        elif self.date < today:
            return "overdue"
        else:
            return "not due yet"

    def show_notification(self):
        n = notify2.Notification(self.name, "Reminder due today")
        n.show()

    def play_alarm(self):
        playsound('alarm.mp3')

def create_reminder():
    name = input("Enter reminder name: ")
    date_str = input("Enter due date (YYYY-MM-DD): ")
    date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    return Reminder(name, date)

reminders = []

while True:
    print("Select an option:")
    print("1. Create a new reminder")
    print("2. Check existing reminders")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        reminder = create_reminder()
        reminders.append(reminder)
        print("Reminder created.")
    elif choice == "2":
        for reminder in reminders:
            status = reminder.check_due_date()
            if status == "due today":
                reminder.show_notification()
                reminder.play_alarm()
            print(f"{reminder.name} is {status}")
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")

    time.sleep(1)