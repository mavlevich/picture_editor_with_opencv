import cv2


def add_india_atmosphere(image):
    # convert the image to LAB color space
    lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

    # separate the L, A, and B channels
    l_channel, a_channel, b_channel = cv2.split(lab_image)

    # increase the saturation of the A and B channels
    a_channel = cv2.add(a_channel, 10)
    b_channel = cv2.add(b_channel, 10)

    # merge the channels back together
    lab_image = cv2.merge((l_channel, a_channel, b_channel))

    # convert the image back to BGR color space
    result = cv2.cvtColor(lab_image, cv2.COLOR_LAB2BGR)

    # increase the contrast of the image
    result = cv2.convertScaleAbs(result, alpha=1.5, beta=0)

    return result


# read the image as a numpy array
img = cv2.imread('image.jpg')

# pass the numpy array to the function
img_processed = add_india_atmosphere(img)

# display the processed image
cv2.imshow('Processed Image', img_processed)
cv2.waitKey(0)
