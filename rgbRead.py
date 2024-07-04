from PIL import Image

def rgb2hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

img = Image.open('image.jpg')

if img.mode in ('RGB', 'LA') or (img.mode == 'P' and 'transparency' in img.info):   
    pixels = list(img.convert('RGBA').getdata())
    for r, g, b, a in pixels: # just ignore the alpha channel
       print(rgb2hex(r, g, b))