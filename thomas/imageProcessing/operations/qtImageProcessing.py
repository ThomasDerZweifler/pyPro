from PyQt5.QtGui import QImage, QColor

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