import random
import tkinter as tk

# Define the GUI window
window = tk.Tk()
window.geometry("200x200")
window.title("Virtual Dice")

# Define the label to display the dice result
result_label = tk.Label(window, text="", font=("Helvetica", 72))
result_label.pack()

# Define the function to roll the dice
def roll_dice():
    # Generate a random number between 1 and 6
    number = random.randint(1, 6)
    # Update the label with the result
    result_label.config(text=str(number))

# Define the button to roll the dice
roll_button = tk.Button(window, text="Roll Dice", command=roll_dice)
roll_button.pack()

# Start the GUI main loop
window.mainloop()
