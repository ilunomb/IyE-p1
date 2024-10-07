import math
matriz = [[1/8, 1/16, 1/32, 1/32], [1/16, 1/8, 1/32, 1/32], [1/16, 1/16, 1/16, 1/16], [1/4, 0, 0, 0]]
p_y = [0.5, 0.25, 0.125, 0.125]
p_x = [0.25, 0.25, 0.25, 0.25]
info_mutua = 0 

for x in range(4):
    for y in range(4):
        if matriz[x][y] != 0:
            info_mutua += matriz[x][y] * math.log2(matriz[x][y] / (p_x[x] * p_y[y]))

print(info_mutua)