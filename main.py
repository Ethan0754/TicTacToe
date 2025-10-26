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
player_turn=1

def get_board_texts():
    return [btn.cget("text") for btn in buttons]

def on_click(b):
    global player_turn

    #Player Move
    if player_turn == 1 and b.cget("text") == "":
        player_turn = 1
        b.config(text = "X")
    else:
        return
    winner = check_winner(get_board_texts())
    if winner == "X":
        buttons[4].config(text="You Win!")
        player_turn = 1
    elif winner == "O":
        buttons[4].config(text="You Lose!")
    elif winner == 0:
        buttons[4].config(text="Tie!")


    #AI Move
    board = get_board_texts()
    _, move = minimax(board, False)  # start with AI move
    if move is not None:
        buttons[move].config(text="O")
    winner = check_winner(get_board_texts())
    if winner == "X":
        buttons[4].config(text="You Win!")
        player_turn = 1
    elif winner == "O":
        buttons[4].config(text="You Lose!")
    elif winner == 0:
        buttons[4].config(text="Tie!")


def check_winner(board):
    board = np.array(board).reshape((3,3))

    # Check row
    for row in board:
        if row[0] != "" and row[0] == row[1] == row[2]:
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] != "" and board[0][col] == board[1][col] == board[2][col]:
            return board[0][col]

    # Check diagonals
    if board[0][0] != "" and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] != "" and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]

    if "" not in board:
        return 0

    return None  # No winner yet

def minimax(board, is_player_turn):
    winner = check_winner(board)
    if winner == "X":
        return 1, None
    elif winner == "O":
        return -1, None
    elif winner == 0:  # tie
        return 0, None

    best_score=-999
    best_move=None
    if is_player_turn:
        for i, cell in enumerate(board):
            if cell == "":
                board[i] = "X"
                score, _ = minimax(board, False)
                board[i] = ""
                if score > best_score:
                    best_score = score
                    best_move = i
                    if best_score == 1:
                        break
        return best_score, best_move
    else:
        best_score = 999
        best_move = None
        for i, cell in enumerate(board):
            if cell == "":
                board[i] = "O"
                score, _ = minimax(board, True)
                board[i] = ""
                if score < best_score:
                    best_score = score
                    best_move = i
                    if best_score == -1:
                        break
        return best_score, best_move


def reset_board():
    global player_turn
    for btn in buttons:
        btn.config(text="")
    player_turn = 1


buttons=[]
for i in range(3):
    for j in range(3):
        btn = ttk.Button(frm, text="", style="Tic.TButton")
        btn.grid(column=j, row=i, padx=10, pady=10)  # Pass button reference to handler
        buttons.append(btn)
for i in range(9):
    buttons[i].config(command=lambda b=buttons[i]: on_click(b))

reset_btn = ttk.Button(root, text="Reset", command=reset_board)
reset_btn.grid(row=2, column=0, pady=10)

root.mainloop()