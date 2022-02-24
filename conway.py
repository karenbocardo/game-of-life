"""
conway.py 
A simple Python/matplotlib implementation of Conway's Game of Life.
"""

import sys, argparse
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
from configurations import *

ON = 255
OFF = 0
vals = [ON, OFF]

filename = "reports/report5.txt"

gens = 200 # generations
curr = 0

def initCounters():
    # initialize counter
    for elem in ALL_CONFIGS:
        counters[elem.name] = 0

def sameMatrix(A,B,w,h):
    for i in range(w):
        for j in range(h):
            if (A[i][j] != B[i][j]):
                return False
    return True

def randomGrid(N):
    """returns a grid of NxN random values"""
    return np.random.choice(vals, N*N, p=[0.2, 0.8]).reshape(N, N)

def addGlider(i, j, grid):
    """adds a glider with top left cell at (i, j)"""
    glider = np.array([[0,    0, 255], 
                       [255,  0, 255], 
                       [0,  255, 255]])
    grid[i:i+3, j:j+3] = glider

def update(frameNum, img, grid, visited, N):
    global curr

    if curr > gens:
        exit()

    # copy grid since we require 8 neighbors for calculation
    # and we go line by line 
    newGrid = grid.copy()
    initCounters()

    for i in range(N):
        for j in range(N):
            # check configurations that exist
            if not visited[i,j]:
                visited[i, j] = 1
                for elem in ALL_CONFIGS:

                    for configuracion in elem.conf:
                        ancho, alto = len(configuracion), len(configuracion[0])

                        if i + ancho + 1 > N or j + alto + 1 > N: continue

                        # add marco de cuadros vacios
                        arr = np.array(configuracion)
                        newArr = np.zeros((ancho+2, alto+2))
                        newArr[1:ancho+1, 1:alto+1] = arr




                        if sameMatrix(newArr, grid[i:i+ancho+2, j:j+alto+2],ancho+1,alto+1):
                            #print("comparando")
                            #print(newArr)
                            #print(grid[i:i+ancho+2, j:j+alto+2])
                            counters[elem.name] += 1
                            for x in range(i, i+ancho+1):
                                for y in range(j, j + alto + 1):
                                    visited[x,y]=1



            # compute 8-neighbor sum
            # using toroidal boundary conditions - x and y wrap around
            # so that the simulaton takes place on a toroidal surface.
            total = int((grid[i, (j - 1) % N] + grid[i, (j + 1) % N] +
                         grid[(i - 1) % N, j] + grid[(i + 1) % N, j] +
                         grid[(i - 1) % N, (j - 1) % N] + grid[(i - 1) % N, (j + 1) % N] +
                         grid[(i + 1) % N, (j - 1) % N] + grid[(i + 1) % N, (j + 1) % N]) / 255)

            # apply Conway's rules
            if grid[i, j] == ON:
                if (total < 2) or (total > 3):
                    newGrid[i, j] = OFF
            else:
                if total == 3:
                    newGrid[i, j] = ON

    curr += 1

    # save report
    print(counters)
    f = open(filename, "a")
    total = 0
    for key in counters:
        total += counters[key]
    f.write("iteration: {}\n".format(curr))
    f.write("---------------------------------------------\n")
    f.write("|			|	count   	|	percent	    |\n")
    f.write("|-----------+---------------+---------------|\n")
    for key, value in counters.items():
        cadena = key.ljust(10)
        cadena_val = str(value).ljust(6)
        perc = 0.0
        if total > 0:
            perc = float(value)  / total *  100
        cadena_perc = "{:.2f}".format(perc).ljust(6)
        f.write("|{}\t|\t{}\t\t|\t{}\t\t|\n".format(cadena, cadena_val, cadena_perc))
    f.write("|-----------+---------------+---------------|\n")
    cadena_total = str(total).ljust(6)
    f.write("|total      |\t{}\t\t|               |\n".format(cadena_total))
    f.write("---------------------------------------------\n")
    f.write("\n")
    f.close()

    # restart visited
    for i in range(N):
        for j in range(N):
            visited[i,j]=0

    # update data
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img,

# main() function
def main():
    global gens
    f = open(filename, "w")
    f.close()

    # Command line args are in sys.argv[1], sys.argv[2] ..
    # sys.argv[0] is the script name itself and can be ignored
    # parse arguments
    parser = argparse.ArgumentParser(description="Runs Conway's Game of Life system.py.")

    # TODO: add arguments
    parser.add_argument('--size', dest='N', required=False)
    parser.add_argument('--input', dest='input', required=False)
    parser.add_argument('--interval', dest='interval', required=False)
    parser.add_argument('--glider', action='store_true', required=False)
    args = parser.parse_args()


    # set grid size
    N = 100
    if args.N and int(args.N) > 8:
        N = int(args.N)
        
    # set animation update interval
    updateInterval = 50
    if args.interval:
        updateInterval = int(args.interval)

    # declare grid
    grid = np.array([])
    visited = np.array([])

    '''
    # populate grid with random on/off - more off than on
    grid = randomGrid(N)
    # Uncomment lines to see the "glider" demo
    #grid = np.zeros(N*N).reshape(N, N)
    #addGlider(1, 1, grid)
    '''

    # check if "glider" demo flag is specified
    if args.glider:
        grid = np.zeros(N * N).reshape(N, N)
        visited = np.zeros(N * N).reshape(N, N)
        addGlider(1, 1, grid)
    elif args.input:
        f = open(args.input, "r")
        lines = f.readlines()

        w,h = lines[0].split()
        w,h = int(w), int(h)
        N = w

        gens = int(lines[1])

        grid = np.zeros(w * h).reshape(w, h)
        visited = np.zeros(w * h).reshape(w, h)

        for line in lines[2:]:
            i, j = line.split()
            i,j = int(i), int(j)
            grid[i,j] = ON


    else:  # populate grid with random on/off -
        # more off than on
        grid = randomGrid(N)
        visited = np.zeros(N * N).reshape(N, N)

    # set up animation
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, visited, N, ),
                                  frames = 10,
                                  interval=updateInterval,
                                  save_count=gens)

    # saving to m4 using ffmpeg writer
    writervideo = animation.FFMpegWriter(fps=1)
    ani.save('video.mp4', writer=writervideo)

    plt.show()

# call main
if __name__ == '__main__':
    main()