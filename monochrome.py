import cv2
import numpy as np


def pastel_monochrome(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to pastel
    pastel = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    pastel = cv2.cvtColor(pastel, cv2.COLOR_GRAY2BGR)

    # Convert the image to monochrome
    monochrome = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    monochrome = cv2.cvtColor(monochrome, cv2.COLOR_GRAY2BGR)

    # Combine the pastel and monochrome images using weighted addition
    output = cv2.addWeighted(pastel, 0.5, monochrome, 0.5, 0)

    # return output

    # Show the pixelated image
    cv2.imshow('mono', output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


pastel_monochrome('image.jpg')