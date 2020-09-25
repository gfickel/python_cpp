import time
import numpy as np
from PIL import Image

from contrast_image import contrast_image
from naive_contrast_image import naive_contrast_image

im = Image.open('images/turing.jpg')
im = np.array(im)

begin = time.time()
for i in range(10):
    contrast_im = contrast_image(im)
print('Mean runtime cpp', (time.time()-begin)*1000/10, 'ms')

begin = time.time()
for i in range(10):
    contrast_im = naive_contrast_image(im)
print('Mean runtime naive', (time.time()-begin)*1000/10, 'ms')

comb = np.zeros((im.shape[0],im.shape[1]*2), dtype=np.uint8)
comb[:,0:im.shape[1]] = im
comb[:,im.shape[1]:] = contrast_im

comb_im = Image.fromarray(comb)
comb_im.save('images/turing_gal.png')
