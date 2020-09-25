import numpy as np

def naive_contrast_image(image):
    result = np.zeros(image.shape, dtype=np.uint8)
    min_color, max_color = np.min(image), np.max(image)
    delta_color = max_color-min_color
    for row in range(image.shape[0]):
        for col in range(image.shape[1]):
            pixel = image[row,col]
            result[row,col] = 255*(pixel-min_color)/delta_color

    return result
