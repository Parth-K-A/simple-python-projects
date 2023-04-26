import tkinter as tk
import random

# Define the function to handle player's choice
def player_choice(choice):
    # Disable all buttons after player has made a choice
    rock_button.config(state=tk.DISABLED)
    paper_button.config(state=tk.DISABLED)
    scissors_button.config(state=tk.DISABLED)

    # Generate computer's choice randomly
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    # Determine the winner and update the result label
    if choice == computer_choice:
        result_label.config(text="It's a tie!")
    elif choice == "rock" and computer_choice == "scissors" \
            or choice == "paper" and computer_choice == "rock" \
            or choice == "scissors" and computer_choice == "paper":
        result_label.config(text="You win!")
    else:
        result_label.config(text="Computer wins!")

# Create the main window
root = tk.Tk()
root.title("Rock Paper Scissors")

# Create the game title label
title_label = tk.Label(root, text="Rock Paper Scissors", font=("Helvetica", 24))
title_label.pack(pady=10)

# Create the button frame
button_frame = tk.Frame(root)
button_frame.pack()

# Create the rock button
rock_button = tk.Button(button_frame, text="Rock", font=("Helvetica", 14), padx=10, pady=5,
                        command=lambda: player_choice("rock"))
rock_button.pack(side=tk.LEFT, padx=10)

# Create the paper button
paper_button = tk.Button(button_frame, text="Paper", font=("Helvetica", 14), padx=10, pady=5,
                         command=lambda: player_choice("paper"))
paper_button.pack(side=tk.LEFT, padx=10)

# Create the scissors button
scissors_button = tk.Button(button_frame, text="Scissors", font=("Helvetica", 14), padx=10, pady=5,
                            command=lambda: player_choice("scissors"))
scissors_button.pack(side=tk.LEFT, padx=10)

# Create the result label
result_label = tk.Label(root, text="", font=("Helvetica", 18), pady=10)
result_label.pack()

# Run the main loop
root.mainloop()
