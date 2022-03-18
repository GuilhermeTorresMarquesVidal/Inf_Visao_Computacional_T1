import numpy as np

from .params import epsilon, count_limit

def threshold_mean(image):
    
    intensity = image.ravel()
    
    threshold = np.mean(intensity)
    mu1 = np.mean(intensity[intensity > threshold])
    mu2 = np.mean(intensity[intensity < threshold])
    threshold_old = threshold
    threshold = 1/2*(mu1+mu2)
    
    count = 0
    
    while(abs(threshold - threshold_old) > epsilon and count < count_limit):
        mu1 = np.mean(intensity[intensity > threshold])
        mu2 = np.mean(intensity[intensity < threshold])
        threshold_old = threshold
        threshold = 1/2*(mu1+mu2)
        count += 1
        
    return threshold