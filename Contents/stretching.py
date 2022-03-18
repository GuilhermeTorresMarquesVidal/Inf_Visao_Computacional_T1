import numpy as np

from .params import grayscale_limit

def linear_stretching(image):
    
    maximum = np.max(image)
    minimum = np.min(image)
    
    return ((image - minimum)/(maximum - minimum)*grayscale_limit).astype(
        np.int32)