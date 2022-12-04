import cv2
import numpy as np
import os
from PIL import Image


def crop_512_to_224(src_path=r"F:\faceHealing\front\image", save_path=r"F:\faceHealing2D_dataset\image\train"):
    """
       1    |   2   |   3 
            |       |
    -------------------------
       4    |   5   |   6
            |       |
    -------------------------
       7    |   8   |   9
            |       |
    """
    for filename in os.listdir(src_path):
        img = Image.open(os.path.join(src_path, filename))
        (left, upper, right, lower) = (0, 0, 224, 224)
        for i in range(3):
            for j in range(3):
                img.crop((left, upper, right, lower)).save(os.path.join(
                    save_path, f"{filename.split('.')[0]}_{i}_{j}.png"))
                left += 144
                right += 144
            (left, right) = (0, 224)
            upper += 144
            lower += 144


fil = np.array([[0, 1, 0],
                [1, 1, 1],
                [0, 1, 0]])


def get_label_from_paint(paint_image, filename):
    mask = np.array(paint_image)
    temp = np.logical_and(mask[:, :, 1] == 177,
                          mask[:, :, 0] == 34).astype(np.uint8)
    temp = cv2.filter2D(temp, -1, fil)
    temp = (temp > 0).astype(np.uint8)*255
    Image.fromarray(temp).save(filename)


def get_label(paint_path, save_path):
    """
    Get label from paint 
    """
    for img_filename in os.listdir(paint_path):
        img = Image.open(os.path.join(paint_path, img_filename))
        get_label_from_paint(img, os.path.join(save_path, img_filename))


# get_label(r"F:\faceHealing\front\label_raw", r"F:\faceHealing\front\label")
# crop_512_to_224(r"F:\faceHealing\dataset\front\label_512",
#                 r"F:\faceHealing\dataset\front\label_224")

def mask_255_to_1(filename, new_filename):
    image = Image.open(filename).convert("L")
    image_arr = np.array(image)
    image_arr = np.where(image_arr > 1, 1, 0)
    Image.fromarray(image_arr).save(new_filename)


def arrange(src_path, save_path, fn):
    for filename in os.listdir(src_path):
        fn(os.path.join(src_path, filename),
           os.path.join(save_path, filename))


arrange(r"C:\codeplace\dataset\faceHealingDataset2D\test\label",
        r"C:\codeplace\dataset\faceHealingDataset2D\test\annotation", mask_255_to_1)
