import numpy as np

from matplotlib import colors as mcolors
from .params import area_minimum, grayscale_limit, SEED

import random as rnd

def paint_segments(images,images_labels,images_labels_count,n_images):

    images_seg = images.copy()

    c = [key for key in mcolors.CSS4_COLORS.keys()]

    for i in range(n_images):
    
        image_labels = np.unique(
            images_labels[i])[1:][images_labels_count[i] > area_minimum]
    
        n_labels = len(image_labels)
        
        rnd.seed(SEED)

        colors_names = rnd.sample(c,n_labels)
    
        for j in range(n_labels):
            images_seg[i][images_labels[i] == image_labels[j]] = (
                np.array(mcolors.to_rgb(
                    colors_names[j]))*grayscale_limit).astype(np.int32)
            
    return images_seg