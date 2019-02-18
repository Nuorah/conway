import numpy as np

def matrixtofile(list):
    with open("matrix.txt", 'w') as file:
        file.write(str(list.shape))
        file.write('\n')
        for line in list:
            for row in line:
                file.write(str(row))
            file.write('\n')
        file.close()

def stringtocouple(string):
    couple = (int(string[1]), int(string[4]))
    return couple

def filetomatrix(filename):
    with open(filename) as file:
        matrix = np.zeros(stringtocouple(file.readline().strip()))
        line = file.readline().strip()
        i = 0
        while(line != ''):
            for j in range(len(line)):
                matrix[i, j-1] = int(line[j-1])
            i = i + 1
            line = file.readline().strip()
        file.close()
        return matrix




