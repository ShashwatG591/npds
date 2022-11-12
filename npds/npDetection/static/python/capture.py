import cv2
from PIL import Image
import pytesseract

camera=cv2.VideoCapture(0)

while True:
    _,image=camera.read()
    cv2.imshow('Text Detection', image)
    if cv2.waitKey(1)& 0xFF==ord('s'):
        cv2.imwrite('test1.jpg', image) 
        break
camera.release()
cv2.distroyAllWindows()

def tesseract():
    path_to_tesseract=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    imagepath='test1.jpg'
    pytesseract.tesseract_cmd=path_to_tesseract
    text=pytesseract.image_to_string(Image.open(imagepath))
    print(text[:-1])
tesseract()