import cv2


def apply_noir_effect(image_path):
    # Load the image using OpenCV
    img = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply a Gaussian blur to the image
    blurred = cv2.GaussianBlur(gray, (0, 0), 3)

    # Invert the blurred image
    inverted = 255 - blurred

    # Apply a Dodge blending mode to the original image and the inverted image
    final_image = cv2.divide(gray, inverted, scale=256)

    # Show the final image
    cv2.imshow('Noir Effect', final_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


apply_noir_effect('image.jpg')
