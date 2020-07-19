import sys
import numpy as np

RGBS = range(16, 255, 16)
CHARS = [' ', '.', ',', ':', ';', '+', '=', 'o',
         'a', 'e', '0', '$', '@', 'A', '#']
FACTORS = [.3, .59, .11]

def main(filename):
    image = open(filename)
    #reads header lines
    color = image.readline()
    _ = image.readline()
    size_width, size_height = image.readline().split()
    max_color = image.readline()

    size_width = int(size_width)
    max_color = int(max_color)

    #reads the body of the file
    data = [int(p) for p in image.read().split()]
    #converts to array and reshape
    data = np.array(data)
    pixels = data.reshape(int(len(data)/3), 3)
    #calculate rgb value per pixel
    rgbs = pixels * FACTORS
    sum_rgbs = rgbs.sum(axis=1)
    rgb_values = [item * 255 / max_color for item in sum_rgbs]

    grayscales = []
    #pulls out the value of each pixel and coverts it to its grayscale value 
    for indx, rgb_val in enumerate(rgb_values):
        #if max width, new line
        if (indx % size_width) == 0 : grayscales.append('\n')    

        for achar, rgb in zip(CHARS, RGBS):
            if rgb_val <= rgb:
                character = achar
                break
            else:
                character = 'M'

        grayscales.append(character)

    print (grayscales)

main('img/test.ppm')