from PIL import Image
import os

filename= "/Users/imge.yazici/Desktop/callcentertickets.jpg"
im = Image.open(filename)
if im.mode == "RGBA" :
    im = im.convert("RGBA")
new_filename= "/Users/imge.yazici/Desktop/callcentertickets.pdf"
if not os.path.exists(new_filename):
    im.save(new_filename,"PDF",resolution=100.0)