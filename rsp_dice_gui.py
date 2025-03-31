import tkinter as tk
import random
import time

# Map moves to emojis
moves = ["rock", "paper", "scissors"]
emojis = {
    "rock": "✊",
    "paper": "✋",
    "scissors": "✌️"
}

# Setup the window
root = tk.Tk()
root.title("Rock Paper Scissors Dice 🎲")
root.geometry("300x350")

# Label to display dice face (emoji)
dice_label = tk.Label(root, text="", font=("Arial", 80))
dice_label.pack(pady=30)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

# Input buttons
def play(user_choice):
    result_label.config(text="")
    # Animate dice roll
    for _ in range(10):
        roll = random.choice(moves)
        dice_label.config(text=emojis[roll])
        root.update()
        time.sleep(0.1)

    computer_choice = roll
    dice_label.config(text=emojis[computer_choice])

    if user_choice == computer_choice:
        result = "🤝 It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        result = "🎉 You win!"
    else:
        result = "😢 You lose."

    result_label.config(text=f"You chose {user_choice}\nComputer chose {computer_choice}\n{result}")

# Buttons
for move in moves:
    btn = tk.Button(root, text=f"{emojis[move]} {move.capitalize()}", font=("Arial", 14),
                    command=lambda m=move: play(m))
    btn.pack(pady=5)

root.mainloop()

