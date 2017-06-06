#!/usr/bin/python

#from __future__ import print_function
from sys import argv
from PIL import Image
import os

script, image_file, width, height = argv


in_im = Image.open(image_file)

#print(im.format, im.size, im.mode)

#m.show()
out_img = in_im.resize((int(width), int(height)), Image.ANTIALIAS)
out_file = os.path.splitext(image_file)[0] + '-{0}X{1}.jpg'.format(width, height)

out_img.save(out_file, "JPEG", quality=100)

out_img.show()
