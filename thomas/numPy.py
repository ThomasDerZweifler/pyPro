from PIL import Image, ImageFilter
#Read image
im = Image.open( 'img/test.png' )
#Display image
im.show()
from PIL import ImageEnhance
enh = ImageEnhance.Contrast(im)
enh.enhance(1.8).show("30% more contrast")