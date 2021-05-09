#!/bin/python3

def nextMove(posr, posc, board):
    c = 0
    a = 0
    b = 0
    for i in range(5):
        for j in range(5):
            if board[i][j] == 'd':
                a,b = i , j
                c = 1
                break
        if c == 1:
            break
    if (posr, posc) == (a,b):
        print("CLEAN")# , a,b,posr,posc)
    else:

        if abs(posr - i) > abs(posc - j) and (posr != i):
            if (posr - i) < 0:
                print("DOWN")
            else:
                print ("UP")# , a,b,posr,posc)
        else:
            
            if (posc - j) < 0:
                print ("RIGHT")#, a,b,posr,posc)
            else:
                print ("LEFT")        


if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    nextMove(pos[0], pos[1], board)