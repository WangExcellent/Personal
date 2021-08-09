# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 20:09:11 2021

@author: ziqin
"""

raw_chess = "         "

chess = [[raw_chess[0], raw_chess[1], raw_chess[2]], [raw_chess[3], raw_chess[4], raw_chess[5]], [raw_chess[6], raw_chess[7], raw_chess[8]]]

print("""---------
| {} {} {} |
| {} {} {} |
| {} {} {} |
---------""".format(chess[0][0], chess[0][1], chess[0][2], chess[1][0], chess[1][1], chess[1][2], chess[2][0], chess[2][1], chess[2][2]))

x = 0
o = 0
t = 0
replay = "Draw"
piece = "X"

def winner():
    global x, o, replay
    if "".join(chess[0]) == "XXX" or "".join(chess[1]) == "XXX" or "".join(chess[2]) == "XXX":
        replay = "X wins"
        x = 1
    elif "".join(chess[:][0]) == "XXX" or "".join(chess[:][1]) == "XXX" or "".join(chess[:][2]) == "XXX":
        replay = "X wins"
        x = 1
    elif "".join([chess[0][0], chess[1][1], chess[2][2]]) == "XXX" or "".join([chess[2][0], chess[1][1], chess[0][2]]) == "XXX":
        replay = "X wins"
        x = 1

    if "".join(chess[0]) == "OOO" or "".join(chess[1]) == "OOO" or "".join(chess[2]) == "OOO":
        replay = "O wins"
        o = 1
    elif "".join(chess[:][0]) == "OOO" or "".join(chess[:][1]) == "OOO" or "".join(chess[:][2]) == "OOO":
        replay = "O wins"
        o = 1
    elif "".join([chess[0][0], chess[1][1], chess[2][2]]) == "OOO" or "".join([chess[2][0], chess[1][1], chess[0][2]]) == "OOO":
        replay = "O wins"
        o = 1
    return replay

while True:
    a, b = input('Enter the coorninates: ').split()
    if a.isdigit() and b.isdigit():
        a = int(a)
        b = int(b)
        if a < 1 or a > 3 or b < 1 or b > 3:
            print("Coordinates should be from 1 to 3!")
            continue
        elif chess[a-1][b-1] == "X" or chess[a-1][b-1] =="O":
            print("This cell is occupied! Choose another one!")
            continue
        else:
            chess[a-1][b-1] = piece
            if piece == "X":
                piece = "O"
            else:
                piece = "X"
            print("""---------
| {} {} {} |
| {} {} {} |
| {} {} {} |
---------""".format(chess[0][0], chess[0][1], chess[0][2], chess[1][0], chess[1][1], chess[1][2], chess[2][0], chess[2][1], chess[2][2]))
    else:
        print("You should enter numbers!")
        continue
    
    winner()
    if any([x, o]):
        print(replay)
        break
    
    if  all([0 for i in range(3) if " " in chess[i]]):
        print(replay)
        break
    
    
    
    
    



