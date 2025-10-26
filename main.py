from tkinter import *
from tkinter import ttk
import numpy as np
 # Change button text to "X"

root = Tk()
root.title("Tic Tac Toe")
root.geometry("800x400")
style = ttk.Style()
style.configure("Tic.TButton", relief="flat", padding=20, font=("Helvetica", 16))
frm = ttk.Frame(root, padding=20)
frm.grid()
player_turn=0

win_states = [["X", "O", "O", "X", "O", "O", "X", "O", "O"], ["X", "X", "X", "O", "O", "O", "O", "O", "O"], ""]


def on_click(buttons, b):
    global player_turn
    if player_turn == 0:
        player_turn = 0
        b.config(text = "X")
    winner = check_winner(buttons)
    if winner == "X":
        buttons[4].config(text="You Win!")
        player_turn = 1
    elif winner == "O":
        buttons[4].config(text="You Lose!")


def check_winner(buttons):
    board = np.array(buttons).reshape((3,3))
    # Check row
    for row in board:
        if row[0].cget("text") != "" and row[0].cget("text") == row[1].cget("text") == row[2].cget("text"):
            return row[0].cget("text")

    # Check columns
    for col in range(3):
        if board[0][col].cget("text") != "" and board[0][col].cget("text") == board[1][col].cget("text") == board[2][col].cget("text"):
            return board[0][col].cget("text")

    # Check diagonals
    if board[0][0].cget("text") != "" and board[0][0].cget("text") == board[1][1].cget("text") == board[2][2].cget("text"):
        return board[0][0].cget("text")
    if board[0][2].cget("text") != "" and board[0][2].cget("text") == board[1][1].cget("text") == board[2][0].cget("text"):
        return board[0][2].cget("text")

    return None  # No winner yet

def generate_game_tree():
    pass

buttons=[]
for i in range(3):
    for j in range(3):
        btn = ttk.Button(frm, text="", style="Tic.TButton")
        btn.grid(column=j, row=i, padx=10, pady=10)  # Pass button reference to handler
        buttons.append(btn)
for i in range(9):
    buttons[i].config(command=lambda b=buttons[i]: on_click(buttons, b))

root.mainloop()