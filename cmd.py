import os

os.makedirs("./image/train")
os.makedirs("./image/test")
os.makedirs("./label/train")
os.makedirs("./label/test")

# === Image ===
# train
os.system("cp -r /mnt/f/faceHealing/dataset/left/train/image/* ./image/train")
os.system("cp -r /mnt/f/faceHealing/dataset/right/train/image/* ./image/train")
os.system("cp -r /mnt/f/faceHealing/dataset/front/image/* ./image/train")
# test
os.system("cp -r /mnt/f/faceHealing/dataset/left/test/image/* ./image/test")
os.system("cp -r /mnt/f/faceHealing/dataset/right/test/image/* ./image/test")

# === Label ===
# train
os.system("cp -r /mnt/f/faceHealing/dataset/left/train/label/* ./label/train")
os.system("cp -r /mnt/f/faceHealing/dataset/right/train/label/* ./label/train")
os.system("cp -r /mnt/f/faceHealing/dataset/front/label/* ./label/train")
# test
os.system("cp -r /mnt/f/faceHealing/dataset/left/test/label/* ./label/test")
os.system("cp -r /mnt/f/faceHealing/dataset/right/test/label/* ./label/test")



