from collections import defaultdict
from PIL import Image
import numpy as np

def count_colors(img,n):
    img=img.reshape(-1,img.shape[-1])
    color=defaultdict(int)

    for pixel in img:
        rgb=(pixel[0],pixel[1],pixel[2])
        color[rgb]+=1

    sorted_color=sorted(color.items(),key=lambda k_v:k_v[1],reverse=True)
    sorted_color=sorted_color[:n]

    return sorted_color


img=Image.open('papad7.png')
img=np.array(img)
top_colors=count_colors(img,n=50)
print(top_colors)
print(len(top_colors))
