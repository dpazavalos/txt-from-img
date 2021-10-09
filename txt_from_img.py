from sys import argv

import cv2
import pytesseract
import pyperclip

# tess_file = '/usr/bin/tesseract'
tess_file = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

pytesseract.pytesseract.tesseract_cmd = tess_file


# img = cv2.imread('breaking.png')
img = cv2.imread(argv[1])

text = pytesseract.image_to_string(img)
# print(text)
pyperclip.copy(text)

