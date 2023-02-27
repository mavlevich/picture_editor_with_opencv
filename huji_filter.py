import cv2
import numpy as np


def huji_filter(image):
    # Convert to LAB color space
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

    # Split into channels
    l, a, b = cv2.split(lab)

    # Apply CLAHE to L channel
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    l = clahe.apply(l)

    # Merge channels back together
    lab = cv2.merge((l, a, b))

    # Convert back to RGB
    huji = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)

    # Apply contrast stretch
    huji = cv2.convertScaleAbs(huji, alpha=1.2, beta=20)

    return huji


# Read the input image
image = cv2.imread("image.jpg")

# Apply the Huji filter
huji_image = huji_filter(image)

# Display the results
cv2.imshow("Input Image", image)
cv2.imshow("Huji Filter", huji_image)
cv2.waitKey(0)

