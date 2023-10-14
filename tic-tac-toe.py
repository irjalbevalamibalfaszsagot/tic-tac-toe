import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Initialize the game
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Open and convert the image to an ICO icon
image = Image.open('media\BM másolata.png')  # Adjust the path as needed
icon = ImageTk.PhotoImage(image)

# Set the icon for the window
root.tk.call('wm', 'iconphoto', root._w, icon)

player = 'X'
board = [[' ' for _ in range(3)] for _ in range(3)]
player_wins = {'X': 0, 'O': 0}

# Labels to display the score using grid
score_label = tk.Label(root, text=f"X: {player_wins['X']}  O: {player_wins['O']}")
score_label.grid(row=0, column=0, columnspan=3)

# Function to handle button clicks
def on_button_click(row, col):
    global player

    if board[row][col] == ' ':
        buttons[row][col].config(text=player)
        board[row][col] = player

        if check_win(player):
            player_wins[player] += 1
            if player_wins[player] == 5:
                messagebox.showinfo("Tic-Tac-Toe", f"{player} nyeri ezt a kört!")
                player_wins['X'] = 0
                player_wins['O'] = 0
                reset_board()
            else:
                messagebox.showinfo("Tic-Tac-Toe", f"{player} nyeri ezt a kört!")
                reset_board()
            update_score_label()
        elif check_draw():
            messagebox.showinfo("Tic-Tac-Toe", "Döntetlen!")
            reset_board()
        else:
            player = 'O' if player == 'X' else 'X'

def update_score_label():
    score_label.config(text=f"X: {player_wins['X']}  O: {player_wins['O']}")

def check_win(player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def check_draw():
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def reset_board():
    global player, board

    player = 'X'
    board = [[' ' for _ in range(3)] for _ in range(3)]

    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text=' ')

# Create buttons for the game board
buttons = []
for i in range(3):
    button_row = []
    for j in range(3):
        button = tk.Button(root, text=' ', font=('normal', 30), height=1, width=3,
                           command=lambda row=i, col=j: on_button_click(row, col))
        button.grid(row=i+1, column=j)  # Shift row by 1 to avoid overlap with score_label
        button_row.append(button)
    buttons.append(button_row)

# Start the game
root.mainloop()