import cv2


def monochrome(image):

    image = cv2.imread(image)
    cv2.imshow('Original', image)
    cv2.waitKey(0)

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Pixelated', gray_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


monochrome('image.jpg')