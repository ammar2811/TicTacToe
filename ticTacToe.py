from tkinter import *
import random

def next_turn():
    pass 

def check_winner():
    pass

def empty_spaces():
    pass

def new_game():
    pass

window = Tk()
window.title("Tic Tac Toe")
players = ["X", "O"]
player = random.choice(players)
buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

label = Label(text=player + "'s turn", font=("Times New Roman", 30))
label.pack(side=TOP)

reset_button = Button(text="Reset", font=("Times New Roman", 20), command=new_game)
reset_button.pack(side=TOP)

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=("Times New Roman", 30), width=5, height=2,
                                      command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)

window.mainloop()