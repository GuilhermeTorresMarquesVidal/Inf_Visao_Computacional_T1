from .params import area_minimum

import cv2

def contours_filters(images_contours,n_images):

    images_contours_filters = []
    images_contours_areas = []

    for i in range(n_images):
        contours_areas = []
        contours_filters = []
        for j in range(len(images_contours[i])):
            area = cv2.contourArea(images_contours[i][j])
            if area > area_minimum:
                contours_areas.append(area)
                contours_filters.append(images_contours[i][j])
        images_contours_areas.append(contours_areas)
        images_contours_filters.append(contours_filters)
        
    return images_contours_areas, images_contours_filters