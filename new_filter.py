import cv2

def apply_van_gogh_style(img):
    # Convert image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply bilateral filter to smooth out details and preserve edges
    filtered = cv2.bilateralFilter(gray, 7, 50, 50)

    # Apply Laplacian filter to emphasize edges
    edges = cv2.Laplacian(filtered, cv2.CV_8U, ksize=5)

    # Invert the edges to get a "sketch" effect
    edges = 255 - edges

    # Apply stylization to the image using the edges as a mask
    stylized = cv2.stylization(img, img, sigma_s=150, sigma_r=0.25)

    # return stylized

    # Show the pixelated image
    cv2.imshow('stylized', stylized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# read image file into numpy array
img = cv2.imread('image.jpg')

# apply Van Gogh style filter
van_gogh_img = apply_van_gogh_style(img)

# display result
cv2.imshow('Van Gogh Style', van_gogh_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
