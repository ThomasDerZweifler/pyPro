from PIL import Image as img

def halftoning(im):
    rgb_im = im.convert('RGB')
    rgb_im_halftoning = img.new('RGB', im.size, "white")

    return rgb_im_halftoning

def flip_horizontal(im):
    rgb_im = im.convert('RGB')
    rgb_im_flipped = img.new('RGB', im.size, "white")

    y = 0
    while y < im.height:
        x = 0
        while x < im.width: 

            r, g, b = rgb_im.getpixel((x, y))

            newX = im.width-1 - x

            rgb_im_flipped.putpixel((newX, y), (r, g, b))

            x = x+1
        y = y+1

    return rgb_im_flipped

def invert(im) :
    rgb_im = im.convert('RGB')
    rgb_im_inverse = img.new('RGB', im.size, "black")
    y = 0
    while y < im.height:
        x = 0
        while x < im.width: 

            r, g, b = rgb_im.getpixel((x, y))

            newR = 255-r
            newG = 255-g
            newB = 255-b

            rgb_im_inverse.putpixel((x, y), (newR, newG, newB))

            x = x+1
        y = y+1

    return rgb_im_inverse

def gray(im) :
    rgb_im = im.convert('RGB')
    rgb_im_gray = img.new('RGB', im.size, "black")
    y = 0
    while y < im.height:
        x = 0
        while x < im.width: 

            r, g, b = rgb_im.getpixel((x, y))

            #gray = int((r + g + b) / 3)

            gray = int((r * 0.299) + (g * 0.587) + (b * 0.114))

            rgb_im_gray.putpixel((x, y), (gray, gray, gray))

            x = x+1
        y = y+1

    return rgb_im_gray

def alpha(im, alpha) :
    rgb_im = im.convert('RGB')
    rgb_im_alpha = img.new('RGBA', im.size, "black")
    y = 0
    while y < im.height:
        x = 0
        while x < im.width: 

            r, g, b = rgb_im.getpixel((x, y))

            rgb_im_alpha.putpixel((x, y), (r, g, b, alpha))

            x = x+1
        y = y+1

    return rgb_im_alpha

def interlace(im) :
    rgb_im = im.convert('RGB')
    rgb_im_interlace = img.new('RGB', im.size, "black")
    y = 0
    while y < im.height:
        x = 0
        while x < im.width: 

            r, g, b = rgb_im.getpixel((x, y))

            rgb_im_interlace.putpixel((x, y), (r, g, b))

            x = x+1
        y = y+2

    return rgb_im_interlace

def reduce(im) :
    rgb_im = im.convert('RGB')
    rgb_im_reduce = im.convert('RGB')
    y = 0
    yOut = 0
    while y < im.height:
        x = 0
        xOut = int(im.width/2)
        while x < im.width: 

            r, g, b = rgb_im.getpixel((x, y))

            rgb_im_reduce.putpixel((xOut, yOut), (r, g, b))

            x = x+1

            if x % 2 == 0 :
                xOut = xOut + 1

        y = y+1

        if y % 2  == 0 :
            yOut = yOut + 1

    return rgb_im_reduce

def mosaic(im) :
    rgb_im = im.convert('RGB')
    rgb_im_mosaic = img.new('RGB', im.size, "black")
    y = 0
    while y < im.height:
        x = 0
        while x < im.width: 

            r, g, b = rgb_im.getpixel((x, y))

            rgb_im_mosaic.putpixel((x, y), (r, g, b))

            x = x+1
        y = y+1

    return rgb_im_mosaic
