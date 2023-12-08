from tkinter import *
from tkinter import ttk
import random

# Function to handle the end of the game by applying styles to buttons
def endGame(winningButton):
    winningButton.configure(style='GreenBold.TButton')
    for index, button in boardButtons.items():
        if index != secret_number:
            button.configure(style='RedBold.TButton')

# Function to handle button clicks and check if the number is guessed
def mark(indexButton):
    if attempts:
        selectedButton = boardButtons[indexButton]
        if indexButton == secret_number:
            message.set("You guessed the number!")
            messageLabel.configure(background='green', foreground="white")
            endGame(selectedButton)
        else:
            attemptsLabel.set(f"You have {attempts[0] - 1} attempts left")
            message.set("You haven't guessed. Keep trying...")
            selectedButton.configure(state=DISABLED)
            attempts[0] -= 1
        if not attempts[0]:
            message.set("You've run out of attempts. Game over!")
            messageLabel.configure(background='red', foreground="white")
            endGame(boardButtons[secret_number])

# GUI setup
root = Tk()
root.title("Guess the Secret Number")

# Generate a random secret number
secret_number = random.randint(1, 9)

# Variables for dynamic content
message = StringVar()
boardButtons = {}
attemptsLabel = StringVar()
attempts = [3]

# Main frame setup
mainframe = ttk.Frame(root, padding=2)
titleLabel = ttk.Label(mainframe, text="Guess the Secret Number. You have 3 attempts")
attemptsLabelVar = ttk.Label(mainframe, textvariable=attemptsLabel)
messageLabel = ttk.Label(mainframe, textvariable=message)
boardFrame = ttk.Frame(mainframe, padding="5", borderwidth=5, relief="ridge")

# Style setup for buttons
style = ttk.Style()
style.configure('Bold.TButton', font=('TkDefaultFont', 12, 'bold'))
style.configure('GreenBold.TButton', font=('TkDefaultFont', 12, 'bold'), foreground='green')
style.configure('RedBold.TButton', font=('TkDefaultFont', 12, 'bold'), foreground='red')

# Create and layout the buttons in the board frame
for boardRow in range(1, 4):
    for boardCol in range(1, 4):
        boardCount = (boardRow - 1) * 3 + boardCol
        boardText = str(boardCount)
        button = ttk.Button(boardFrame, text=boardText, command=lambda i=boardCount: mark(i), style='Bold.TButton')
        button.grid(column=boardCol, row=boardRow)
        boardButtons[boardCount] = button

# Grid layout for the main frame components
mainframe.grid(column=0, row=0)
titleLabel.grid(column=0, row=0, columnspan=3)
attemptsLabelVar.grid(column=0, row=1, columnspan=3)
messageLabel.grid(column=0, row=2, columnspan=3)
boardFrame.grid(column=0, row=3, columnspan=3, rowspan=3)

# Start the GUI event loop
root.mainloop()
