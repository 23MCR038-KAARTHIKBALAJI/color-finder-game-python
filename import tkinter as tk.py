import tkinter as tk
import random
import time

# List of colors
colors = ['Red', 'Blue', 'Green', 'Pink', 'Black', 'Yellow', 'Orange', 'Purple', 'Brown', 'Gray']
score = 0
time_left = 60

# Function to start the game
def start_game(event=None):
    if time_left == 60:
        countdown()
    next_color()

# Function to display the next color
def next_color():
    global score, time_left

    if time_left > 0:
        # Make the entry box active
        entry.focus_set()

        # Check if the entered text matches the color
        if entry.get().lower() == colors[1].lower():
            score += 1

        # Clear the entry box
        entry.delete(0, tk.END)

        # Shuffle the colors
        random.shuffle(colors)

        # Change the text and the color to display
        color_label.config(fg=colors[1], text=colors[0])

        # Update the score
        score_label.config(text=f"Score: {score}")

# Countdown timer function
def countdown():
    global time_left

    if time_left > 0:
        time_left -= 1
        time_label.config(text=f"Time left: {time_left}s")
        time_label.after(1000, countdown)
    else:
        color_label.config(text="Game Over!", fg="black")
        entry.config(state='disabled')

# Create the main window
root = tk.Tk()
root.title("Color Finder Game")
root.geometry("400x300")

# Add instructions
instructions = tk.Label(root, text="Type the color of the word, not the word itself!", font=('Helvetica', 12))
instructions.pack()

# Add the score label
score_label = tk.Label(root, text=f"Score: {score}", font=('Helvetica', 12))
score_label.pack()

# Add the time left label
time_label = tk.Label(root, text=f"Time left: {time_left}s", font=('Helvetica', 12))
time_label.pack()

# Add the color display label
color_label = tk.Label(root, font=('Helvetica', 24))
color_label.pack()

# Add the entry box for user input
entry = tk.Entry(root, font=('Helvetica', 14))
entry.pack()
entry.bind("<Return>", start_game)

# Add a start button
start_button = tk.Button(root, text="Start", command=start_game)
start_button.pack()

# Run the main event loop
root.mainloop()
