from tkinter import *
import random

# Initialize the main application window
root = Tk()
root.geometry("400x500")
root.title("Dice Roller")
root.configure(bg="#D3E4CD")  # Soft light blue background

# Function to draw a single die face
def draw_dice(canvas, x, y, value):
    # Draw the dice background with rounded corners (using oval for a rounded effect)
    canvas.create_rectangle(x, y, x + 100, y + 100, fill="white", outline="black", width=2)

    # Dot positions for each die face value
    dot_positions = {
        1: [(50, 50)],
        2: [(30, 30), (70, 70)],
        3: [(30, 30), (50, 50), (70, 70)],
        4: [(30, 30), (30, 70), (70, 30), (70, 70)],
        5: [(30, 30), (30, 70), (50, 50), (70, 30), (70, 70)],
        6: [(30, 30), (30, 50), (30, 70), (70, 30), (70, 50), (70, 70)]
    }

    # Draw the dots on the dice
    for idx, dot in enumerate(dot_positions[value], start=1):
        color = "red" if value == 1 and idx == 1 else "black"  # Central dot is red, others black
        canvas.create_oval(
            x + dot[0] - 10, y + dot[1] - 10, x + dot[0] + 10, y + dot[1] + 10,
            fill=color
        )

# Function to roll the dice
def roll():
    # Clear the canvas
    canvas.delete("all")

    # Roll two dice and draw their faces
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    draw_dice(canvas, 50, 100, die1)
    draw_dice(canvas, 200, 100, die2)

    # Display the total roll value
    total_label.config(text=f"Total: {die1 + die2}")

# Create a canvas for drawing dice
canvas = Canvas(root, width=350, height=300, bg="#E8F0F2")  # Light grayish blue canvas
canvas.pack(pady=20)

# Create a label to display the total value
total_label = Label(root, text="Total: ", font=("Helvetica", 16), bg="#D3E4CD", fg="black")
total_label.pack()

# Create a button to roll the dice
button = Button(root, text="Roll Dice", width=15, height=2, font=("Helvetica", 12), bg="white", command=roll)
button.pack(pady=20)

# Run the main application loop
root.mainloop()
