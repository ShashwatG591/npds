#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pytesseract
from PIL import Image
import cv2
import matplotlib.pyplot as plt
import numpy as np


# #For Configuration

# In[ ]:


cam = cv2.VideoCapture(0)
result, image = cam.read()

if result:
    cv2.imshow("demo", image)
    cv2.imwrite("demo.png", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("No image detected. Please! try again")


# In[ ]:


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# In[ ]:


img = cv2.imread('demo.png')


# In[ ]:


plt.imshow(img)


# In[ ]:


img2char = pytesseract.image_to_string(img)


# In[ ]:


print(img2char)


# In[ ]:





# In[ ]:




