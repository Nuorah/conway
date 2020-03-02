import numpy as np
import time
import sys
import os
import argparse
import matplotlib as mpl 
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description="Simple implementation of Conway's game of life.")

parser.add_argument('--height', type=int, help="height of the grid.")
parser.add_argument('--width', type=int, help="width of the grid.")
parser.add_argument('--generations', type=int, help="Number of generations to display, default is infinite.")
parser.add_argument('--speed', type=float, help="Speed at which the generations are displayed in Hertz.")
parser.add_argument('--useConsole', action='store_true', help="Boolean for displaying results in window instead of console")

args = parser.parse_args()

if args.height:
    height = args.height
else:
    height = 50

if args.width:
    width = args.width
else:
    width = 50

if args.speed:
    speed = args.speed
else:
    speed = 5

useWindow = not args.useConsole

grid = np.random.randint(2, size = (height, width))
if useWindow:
    fig = plt.figure()
    im = plt.imshow(grid, cmap='gray')
    plt.axis('off')
    fig.canvas.draw()
    plt.show(block=False)
    fig.canvas.draw()
generation = 0


def sum_around_cell(x, y, grid):
    return grid[x-1, y-1] + grid[x-1, y] + grid[x-1, (y+1) % width] + grid[x, (y+1) % width] + grid[(x+1) % height, (y+1) % width] + grid[(x+1) % height, y] + grid[(x+1) % height, y-1] + grid[x, y-1]


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


def next_grid(grid):
    new_grid = np.zeros((height, width), dtype=int)
    it = np.nditer(grid, flags=['multi_index'])
    while not it.finished:
        new_grid[it.multi_index[0], it.multi_index[1]] = decide_next_cell(it.multi_index[0], it.multi_index[1], grid)
        it.iternext()
    return new_grid

def display(grid):
    if useWindow:
        im.set_data(grid)
        fig.canvas.draw()
    else:
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

if args.generations:
    while generation < args.generations:
        grid = next_grid(grid)
        generation += 1
        print(f"Generation : {generation}")
        display(grid)
        time.sleep(1/speed)
        sys.stdout.flush()
else:
    while True:
        grid = next_grid(grid)
        generation += 1
        print(f"Generation : {generation}")
        display(grid)
        time.sleep(1/speed)
