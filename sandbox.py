#from connect4 import grid
import numpy

grid_in = [['-', 'x', 'o'],
            ['x', 'o', 'o']]
grid2 = [[] for i in range(7)]
grid = grid_in[::-1]

#print(grid_in)
#print(grid)

#for row in reversed(grid):
#    print(*row)

# print(grid[:][1])
# print(grid[1])

# grid2[0].append('o')

# print(grid2)

TOKENS = {'a': 'x', 'b': 'o'}
for key in TOKENS.keys():
    print(key)