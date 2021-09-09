from sys import argv

import cv2
import pytesseract

tess_file = '/usr/bin/tesseract'

pytesseract.pytesseract.tesseract_cmd = tess_file


# img = cv2.imread('breaking.png')
img = cv2.imread(argv[1])

text = pytesseract.image_to_string(img)
print(text)


