import numpy as np
from PIL import Image
import cv2

img = Image.open(r"./data/2.png")
img_paint = Image.open(r"./data/2_paint.png")

img_arr = np.array(img)
img_paint_arr = np.array(img_paint)
# ==================
# diff = img_arr - img_paint_arr[:, :, :3]
# diff = diff[:, :, 1]*2-diff[:, :, 0]-diff[:, :, 2]
# diff = np.where(diff > 255*2-20, 255, 0).astype(np.uint8)

# diff = cv2.dilate(diff, kernel=np.ones((2, 2), dtype=np.uint8), iterations=1)
# ==================
diff = img_paint_arr[:, :, 1]*2-img_paint_arr[:, :, 0]-img_paint_arr[:, :, 2]
diff = np.where(diff > 255*2-20, 255, 0).astype(np.uint8)

Image.fromarray(diff).show()
