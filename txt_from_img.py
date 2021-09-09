import cv2
import pytesseract

tess_file = '/usr/bin/tesseract'

pytesseract.pytesseract.tesseract_cmd = tess_file

img = cv2.imread('breaking.png')

text = pytesseract.image_to_string(img)
print(text)
