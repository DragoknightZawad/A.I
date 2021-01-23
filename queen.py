positions = [[0 for i in range(8)] for j in range(8)]

positions[1][1] = 1
positions[3][3] = 2
positions[2][5] = 3
positions[6][1] = 4
positions[0][2] = 5
positions[7][6] = 6
positions[4][7] = 7
positions[4][0] = 8

def Attacks(x, y):
    for i in range(x+1, 8):
        if positions[i][y] != 0:
            print("Q"+str(positions[i][y]), end=", ")
    for i in range(0, x-1):
        if positions[i][y] != 0:
            print("Q"+str(positions[i][y]), end=", ")
    for i in range(1,8):
        if x+i == 8 or y+i == 8:
            break
        elif positions[x+i][y+i] != 0:
            print("Q"+str(positions[x+i][y+i]), end=", ")
    for i in range(1,8):
        if x-i < 0 or  y+i > 7:
            break
        elif positions[x-i][y+i] != 0:
            print("q"+str(positions[x-i][y+i]), end=", ")
    for i in range(1,8):
        if x-i < 0 or  y-i < 0:
            break
        elif positions[x-i][y-i] != 0:
            print("q"+str(positions[x-i][y-i]), end=", ")
    for i in range(1,8):
        if x+i > 7 or  y-i < 0:
            break
        elif positions[x+i][y-i] != 0:
            print("q"+str(positions[x+i][y-i]), end=", ")
    print()

for k in range(8):
    for i in range(8):
        for j in range(8):
            if positions[i][j] == k+1:
                print("Q"+str(k+1), end=": ")
                Attacks(i,j)
