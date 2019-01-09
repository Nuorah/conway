import numpy as np
import time
import sys
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

np.set_printoptions(threshold=np.nan)
length = 50
width = 50
grid = np.random.randint(2, size = (length, width))
generation = 0


def sum_around_cell(x, y, grid):
    return grid[x-1, y-1] + grid[x-1, y] + grid[x-1, (y+1) % width] + grid[x, (y+1) % width] + grid[(x+1) % length, (y+1) % width] + grid[(x+1) % length, y] + grid[(x+1) % length, y-1] + grid[x, y-1]


def decide_next_cell(x, y, grid):
    sum = sum_around_cell(x, y, grid)
    if grid[x, y] == 0:
        if sum == 3:
            return 1
        else:
            return 0
    else:
        if sum == 2 or sum == 3:
            return 1
        else:
            return 0


apply_decide_next_cell = np.vectorize(decide_next_cell)

def next_grid(grid):
    new_grid = np.zeros((length, width), dtype=int)
    it = np.nditer(grid, flags=['multi_index'])
    while not it.finished:
        new_grid[it.multi_index[0], it.multi_index[1]] = decide_next_cell(it.multi_index[0], it.multi_index[1], grid)
        it.iternext()
    return new_grid

def display(grid):
    it = np.nditer(grid, flags=['multi_index'])
    line = 0
    while not it.finished:
        if line == it.multi_index[0]:
            if it[0] == 1:
                print(u"\u25A1",end=' ')
            else:
                print(u"\u25A0",end= ' ')
            #print(it[0], end='')
        else:
            print('')
            if it[0] == 1:
                print(u"\u25A1", end=' ')
            else:
                print(u"\u25A0", end= ' ')
            line += 1
        it.iternext()
    print('\n')

print(f"Generation : {generation}")
display(grid)

while input != 'exit':
    grid = next_grid(grid)
    generation += 1
    print(f"Generation : {generation}")
    display(grid)
    time.sleep(0.2)
    sys.stdout.flush()
