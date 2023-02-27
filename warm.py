import cv2
import numpy as np

def add_warmer_shades(image, amount):
    image = cv2.imread(image)

    # Convert BGR image to LAB color space
    lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

    # Split channels
    l_channel, a_channel, b_channel = cv2.split(lab_image)

    # Increase a-channel values to add warmth
    a_channel = np.clip(a_channel + amount, 0, 255).astype(np.uint8)

    # Merge channels
    lab_image = cv2.merge((l_channel, a_channel, b_channel))

    # Convert back to BGR color space
    warmer_image = cv2.cvtColor(lab_image, cv2.COLOR_LAB2BGR)

    # return warmer_image

    # Show the pixelated image
    cv2.imshow('warmer_image', warmer_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


add_warmer_shades('image.jpg', 40)
