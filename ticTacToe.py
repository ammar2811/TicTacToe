from tkinter import *
import random

def next_turn(row, column):
    global player

    if buttons[row][column]['text'] == "" and check_winner() is False:
        buttons[row][column]['text'] = player
        if check_winner() is False:
            player = players[1] if player == players[0] else players[0]
            label.config(text=(player + "'s turn"))
        elif check_winner() is True:
            label.config(text=(buttons[row][column]['text'] + " wins!"))
        elif check_winner() == "Tie":
            label.config(text=("Tie!"))
    
    else:
        buttons[row][column]['text'] = player
        if check_winner() is False:
               player = players[0]
               label.config(text=(players[0]+"turn"))
        elif check_winner() is True:
                label.config(text=(players[1]+"wins"))
        elif check_winner() == "Tie":
               label.config(text=("Tie!"))
               
def check_winner():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="blue")
            buttons[row][1].config(bg="blue")
            buttons[row][2].config(bg="blue")
            return True

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="blue")
            buttons[1][column].config(bg="blue")
            buttons[2][column].config(bg="blue")
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="blue")
        buttons[1][1].config(bg="blue")
        buttons[2][2].config(bg="blue")
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="blue")
        buttons[1][1].config(bg="blue")
        buttons[2][0].config(bg="blue")
        return True

    elif empty_spaces() is False:

        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="red")
        return "Tie"

    else:
        return False

def empty_spaces():
    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]["text"] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else: 
        return True

def new_game():
    global player
    player = random.choice(players)
    label.config(text=player + " 's turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#F0F0F0")

window = Tk()
window.title("Tic Tac Toe")
players = ["\U0001F643", "\U0001F607"]
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