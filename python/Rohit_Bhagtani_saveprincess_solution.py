#!/usr/bin/python

def displayPathtoPrincess(n,grid):
    posm = []
    posp = []
    for i in range(n):
        for j in range(n):
            if(grid[i][j] == 'm'):
                posm = [i,j]
            if(grid[i][j] == 'p'):
                posp = [i,j]
    while(posm != posp):
        if(posm[0] < posp[0]):
            print("DOWN")
            posm[0] += 1
        elif(posm[0] > posp[0]):
            print("UP")
            posm[0] -= 1
        elif(posm[1] > posp[1]):
            print("LEFT")
            posm[1] -= 1
        else:
            print("RIGHT")
            posm[1] += 1
#print all the moves here

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())
displayPathtoPrincess(m,grid)