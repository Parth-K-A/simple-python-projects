import tkinter as tk
import random

# Set up the window
window = tk.Tk()
window.title("Snake Water Gun Game")
window.geometry("369x369")
# Set up the variables
player_score = 0
computer_score = 0

# Define the functions
def play_game(player_choice):
    global player_score, computer_score
    computer_choice = random.choice(["snake", "water", "gun"])
    if player_choice == computer_choice:
        result_label.config(text="Tie!")
    elif (player_choice == "snake" and computer_choice == "water") or (player_choice == "water" and computer_choice == "gun") or (player_choice == "gun" and computer_choice == "snake"):
        player_score += 1
        result_label.config(text="You win!")
        player_score_label.config(text=f"Player: {player_score}")
    else:
        computer_score += 1
        result_label.config(text="You lose!")
        computer_score_label.config(text=f"Computer: {computer_score}")

def reset_game():
    global player_score, computer_score
    player_score = 0
    computer_score = 0
    player_score_label.config(text=f"Player: {player_score}")
    computer_score_label.config(text=f"Computer: {computer_score}")
    result_label.config(text="")

# Create the GUI
label1 = tk.Label(text="Choose your weapon:")
label1.pack()

button1 = tk.Button(text="Snake", command=lambda: play_game("snake"))
button1.pack()

button2 = tk.Button(text="Water", command=lambda: play_game("water"))
button2.pack()

button3 = tk.Button(text="Gun", command=lambda: play_game("gun"))
button3.pack()

result_label = tk.Label(text="")
result_label.pack()

score_frame = tk.Frame()
score_frame.pack()

player_score_label = tk.Label(master=score_frame, text=f"Player: {player_score}")
player_score_label.pack(side=tk.LEFT)

computer_score_label = tk.Label(master=score_frame, text=f"Computer: {computer_score}")
computer_score_label.pack(side=tk.RIGHT)

reset_button = tk.Button(text="Reset", command=reset_game)
reset_button.pack()

# Start the GUI
window.mainloop()
