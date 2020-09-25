import ctypes
import numpy as np
from numpy.ctypeslib import ndpointer

lib = ctypes.CDLL('./libcontrast_image.so')

c_contrast_image = lib.cpp_contrast_image
c_contrast_image.argtypes = [
    ndpointer(ctypes.c_ubyte, flags='C_CONTIGUOUS'),
    ctypes.c_int,
    ctypes.c_int,
    ndpointer(ctypes.c_ubyte, flags='C_CONTIGUOUS'),
]

def contrast_image(image):
    result = np.zeros(image.shape, dtype=np.uint8)
    c_contrast_image(image, image.shape[0], image.shape[1], result)
    return result
