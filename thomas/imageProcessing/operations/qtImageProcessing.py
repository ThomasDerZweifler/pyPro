
from PyQt5.QtGui import QImage, QColor

def invert(qImage) :
    rgb_im_inverse = qImage.copy()
    y = 0
    while y < qImage.height():
        x = 0
        while x < qImage.width(): 

            color = QColor.fromRgb(qImage.pixel(x, y))

            newR = 255-color.red()
            newG = 255-color.green()
            newB = 255-color.blue()

            newColor = QColor(newR,newG,newB)

            rgb_im_inverse.setPixel(x, y, newColor.rgba())

            x = x+1
        y = y+1

    return rgb_im_inverse