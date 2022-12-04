import os
from PIL import Image
import numpy as np
import cv2

fil = np.array([[0, 1, 0],
                [1, 1, 1],
                [0, 1, 0]])

mk = np.array(Image.open(r"./data/2_paint.png"))
temp = np.logical_and(mk[:, :, 1] == 177,
                      mk[:, :, 0] == 34).astype(np.uint8)
temp = cv2.filter2D(temp, -1, fil)
temp = (temp > 0).astype(np.uint8)*255
Image.fromarray(temp).show()
