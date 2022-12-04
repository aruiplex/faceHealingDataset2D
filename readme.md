# FaceHealing Dataset 2D

```
.
├── cmd.py  # copy src directories to target
├── dev     # developing code 
│   ├── a.py
│   ├── b.py
│   ├── process.py
│   └── readme.md
├── preprocess.py   # functions to get 512 to 224, get annotation track, {0, 255} annotation to {0, 1}       
|                     annotation
├── readme.md       # introduction
├── test            # test dataset 
│   ├── annotation  # {0, 1} annotation for MMCV used 
│   ├── image       # test images, only contains 2 views: right and left. 
│   └── label       # {0, 255} annotation
└── train           # train dataset 
    ├── annotation  # {0, 1} annotation for MMCV used 
    ├── image       # train images, contains 3 views: front, left, right 
    └── label       # {0, 255} annotation

9 directories, 7 files
```

