import numpy as np
import matplotlib.pyplot as plt
from utils import ade_palette

def draw_mask(seg, image):
    color_seg = np.zeros((seg.shape[0], seg.shape[1], 3), dtype=np.uint8)  # height, width, 3
    palette = np.array(ade_palette())
    color_seg[seg == 1, :] = palette[1]
    color_seg = color_seg[..., ::-1]

    img = np.array(image) * 0.5 + color_seg * 0.5
    plt.figure(figsize=(15, 10))
    plt.imshow(img)
    plt.show()
