import cv2


def reduce_brightness(img, percentage):
    """
    Reduces the brightness of an image by a specified percentage.
    :param img: The input image as a NumPy array.
    :param percentage: The percentage to reduce the brightness by (0 to 100).
    :return: The image with reduced brightness.
    """
    # Convert the image to the HSV color space.
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Split the channels.
    h, s, v = cv2.split(hsv)

    # Apply the brightness reduction.
    v = cv2.subtract(v, int((percentage / 100) * 255))

    # Make sure the values are in the valid range.
    v = cv2.max(v, 0)
    v = cv2.min(v, 255)

    # Merge the channels back together.
    hsv = cv2.merge((h, s, v))

    # Convert the image back to the original color space.
    return cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)


# Load the image.
img = cv2.imread('image.jpg')

# Reduce the brightness by n%.
img = reduce_brightness(img, 25)

# Display the result.
cv2.imshow('Reduced Brightness', img)
cv2.waitKey(0)
cv2.destroyAllWindows()