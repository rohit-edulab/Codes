#path.append(l)
    #path.append(m)

a = 0
b = 0
count = 0
def nextMove(n,r,c,grid):
    
    if(r-a) > 0 :
        return "UP"
    elif(r-a) < 0:
        return "DOWN"
    elif(c-b) > 0:
        return "LEFT"
    elif(c-b) < 0:
        return "RIGHT"
    else:
        return ""
   
    
    return path

n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())
for i in range(0,n):
        for j in range(0,n):
            if(grid[i][j] == 'p'):
                b = j
                a = i
                count = 1
                break
        if count == 1:
            break
print(nextMove(n,r,c,grid))