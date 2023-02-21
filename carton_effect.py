import cv2


def carton_effect(image):
    image = cv2.imread(image)
    # Apply the bilateral filter
    num_down = 2  # Number of downsampling steps
    num_bilateral = 7  # Number of bilateral filtering steps

    # Apply multiple downsampling steps
    for i in range(num_down):
        image = cv2.pyrDown(image)

    # Apply the bilateral filter multiple times
    for i in range(num_bilateral):
        image = cv2.bilateralFilter(image, d=9, sigmaColor=9, sigmaSpace=7)

    # Upsample the image back to its original size
    for i in range(num_down):
        image = cv2.pyrUp(image)

    # Display the image
    cv2.imshow('Cartoon Effect', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save the image
    # cv2.imwrite('cartoon_image.jpg', image)


carton_effect('image.jpg')
