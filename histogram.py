import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('cat.jpg',0)
cv2.imshow('image',img)
plt.hist(img.ravel(),256,[0,256])
plt.show()


cv2.waitKey()
cv2.destroyAllWindows()