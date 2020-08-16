from PyQt5.QtGui import QImage, QColor

import sympy as sp
def tand(x):
    return sp.tan(x * sp.pi / 180)

def sind(x):
    return sp.sin(x * sp.pi / 180)

def cosd(x):
    return sp.cos(x * sp.pi / 180)

def invert(qImage) :
    rgb_im_inverse = qImage.copy()
    width = qImage.width()
    y = 0
    while y < qImage.height():
        x = 0
        while x < width: 
            color = QColor.fromRgb(qImage.pixel(x, y))
            newR = 255-color.red()
            newG = 255-color.green()
            newB = 255-color.blue()
            newColor = QColor(newR,newG,newB)
            rgb_im_inverse.setPixel(x, y, newColor.rgba())
            x = x+1
        y = y+1
    return rgb_im_inverse

def flip_horizontal(qImage):
    rgb_im_flipped = qImage.copy()
    width = qImage.width()
    y = 0
    while y < qImage.height():
        x = 0
        while x < width: 
            color = QColor.fromRgb(qImage.pixel(x, y))
            newX = width-1 - x
            rgb_im_flipped.setPixel(newX, y, color.rgba())
            x = x+1
        y = y+1
    return rgb_im_flipped

def interlace(qImage) :
    rgb_im_interlace = qImage.copy()
    rgb_im_interlace.fill(0)
    width = qImage.width()
    y = 0
    while y < qImage.height():
        x = 0
        while x < width: 
            color = QColor.fromRgb(qImage.pixel(x, y))
            rgb_im_interlace.setPixel(x, y, color.rgba())
            x = x+1
        y = y+2
    return rgb_im_interlace

def gray(qImage) :
    rgb_im_gray = qImage.copy()
    width = qImage.width()
    y = 0
    while y < qImage.height():
        x = 0
        while x < width: 
            color = QColor.fromRgb(qImage.pixel(x, y))
            r = color.red()
            g = color.green()
            b = color.blue()

            #gray = int((r + g + b) / 3)

            gray = int((r * 0.299) + (g * 0.587) + (b * 0.114))

            newColor = QColor(gray,gray,gray)
            rgb_im_gray.setPixel(x, y, newColor.rgba())
            x = x+1
        y = y+1

    return rgb_im_gray

def reduce(qImage) :
    rgb_im_reduce = qImage.copy()
    width=qImage.width()
    y = 0
    yOut = 0
    while y < qImage.height():
        x = 0
        xOut = int(width/2)
        while x < width: 

            color = QColor.fromRgb(qImage.pixel(x, y))
            rgb_im_reduce.setPixel(xOut, yOut, color.rgba())

            x = x+1

            if x % 2 == 0 :
                xOut = xOut + 1

        y = y+1

        if y % 2  == 0 :
            yOut = yOut + 1

    return rgb_im_reduce

def mosaic(qImage, pixelSize) :
    rgb_im_mosaic = qImage.copy()
    width=qImage.width()

    y = 0
    while y < qImage.height():
        if y % pixelSize == 0:
            ry = y

        x = 0
        while x < width: 
            if x % pixelSize == 0:
                rx = x
                color = QColor.fromRgb(rgb_im_mosaic.pixel(rx, ry))
                
            rgb_im_mosaic.setPixel(x, y, color.rgba())

            x = x+1
        
        y = y+1

    return rgb_im_mosaic

def rotate(qImage, angle) :
    rgb_im_rotated = qImage.copy()
    rgb_im_rotated.fill(0)
    width = qImage.width()
    height = qImage.height()
    y = 1
    while y < height:
        x = 1
        while x < width: 

            inputRow = y * cosd(angle) - x * sind(angle)
            inputCol = y * sind(angle) + x * cosd(angle)

            if inputRow >= 0 and inputRow < height and inputCol >= 0 and inputCol < width:
                color = QColor.fromRgb(qImage.pixel(inputCol, inputRow))
                rgb_im_rotated.setPixel(x, y, color.rgba())

            x = x+5
        y = y+5
    return rgb_im_rotated
 