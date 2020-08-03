from PIL import Image as img

import operations.imageProcessing as imgProc

im = img.open("img/cinzano.ppm")

print( str(im.width) + ", " + str(im.height))

im.show()

#imgProc.invert(im).show()

#imgProc.gray(im).show()

#imgProc.alpha(im, 100).show()

#imgProc.interlace(im).show()

#imgProc.reduce(im).show()

#imgProc.halftoning(im).show()

imgProc.flip_horizontal(im).show()
