import matplotlib.pyplot as plt
import os
from PIL import Image
import numpy as np

import cv2
fil = np.array([[0, 1, 0],
                [1, 1, 1],
                [0, 1, 0]])


os.makedirs('train/image', exist_ok=True)
os.makedirs('train/mask', exist_ok=True)

os.makedirs('test/image', exist_ok=True)
os.makedirs('test/mask', exist_ok=True)

for f in os.listdir('faceHealing_dataset_skin_label/train'):
    mk = np.array(Image.open(os.path.join(
        'faceHealing_dataset_skin_label/train', f)).convert('RGB'))
    im = np.array(Image.open(os.path.join(
        'faceHealing_dataset_skin_source', f)).convert('RGB'))
    temp = np.logical_and(mk[:, :, 1] == 177,
                          mk[:, :, 0] == 34).astype(np.uint8)
    temp = cv2.filter2D(temp, -1, fil)
    temp = (temp > 0).astype(np.uint8)*255
    Image.fromarray(temp).save(os.path.join('train/mask', f))
    Image.fromarray(im).save(os.path.join('train/image', f))

    # print(mk.dtype,mk.shape)
    # plt.subplot(221)
    # plt.imshow(mk)
    # plt.subplot(222)
    #
    # plt.imshow(temp)
    # plt.subplot(223)
    # mk[temp]=np.array([255,0,0])
    # plt.imshow(mk)
    # plt.subplot(224)
    # plt.imshow(im)
    # plt.show()
for f in os.listdir('faceHealing_dataset_skin_label/test'):
    mk = np.array(Image.open(os.path.join(
        'faceHealing_dataset_skin_label/test', f)).convert('RGB'))
    im = np.array(Image.open(os.path.join(
        'faceHealing_dataset_skin_source', f)).convert('RGB'))
    temp = np.logical_and(mk[:, :, 1] == 177,
                          mk[:, :, 0] == 34).astype(np.uint8)
    temp = cv2.filter2D(temp, -1, fil)
    temp = (temp > 0).astype(np.uint8)*255
    Image.fromarray(temp).save(os.path.join('test/mask', f))
    Image.fromarray(im).save(os.path.join('test/image', f))
