import cv2
import numpy as np


# kernel_size - degree of blurring
def apply_motion_effect(img, kernel_size=60):
    # Create motion blur kernel
    kernel = np.zeros((kernel_size, kernel_size))
    kernel[int((kernel_size-1)/2), :] = np.ones(kernel_size)
    kernel = kernel / kernel_size

    # Apply motion blur filter
    motion_blur = cv2.filter2D(img, -1, kernel)
    return motion_blur



img = cv2.imread('image.jpg')
motion_blur_img = apply_motion_effect(img)
cv2.imshow('Motion Blur', motion_blur_img)
cv2.waitKey(0)

