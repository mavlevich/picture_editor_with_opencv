import cv2

def increase_resolution(image_path):
    # Load image from file
    img = cv2.imread(image_path)

    # Get the original image size
    height, width, _ = img.shape

    # Create a new image with twice the resolution
    new_width = width * 2
    new_height = height * 2
    new_img = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_LINEAR)

    # Show the result
    cv2.imshow('Increased Resolution', new_img)
    cv2.waitKey(0)

    # Save the result to a file
    cv2.imwrite('increased_resolution.jpg', new_img)


increase_resolution('image2.jpg')
