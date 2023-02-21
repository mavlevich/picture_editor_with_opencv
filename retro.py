import cv2
import numpy as np

def retro_effect(image_path):
    # Load the image
    img = cv2.imread(image_path)

    # Create a copy of the image
    retro = np.copy(img)

    # Split the image into its BGR channels
    b, g, r = cv2.split(retro)

    # Apply a Gaussian blur to the blue channel
    b = cv2.GaussianBlur(b, (0, 0), 15)

    # Merge the channels back into an image
    retro = cv2.merge((b, g, r))

    # Apply a sepia filter to the image
    kernel = np.array([[0.393, 0.769, 0.189],
                       [0.349, 0.686, 0.168],
                       [0.272, 0.534, 0.131]])
    sepia = cv2.transform(retro, kernel)

    # Increase the contrast of the image
    alpha = 1.2
    beta = 10
    contrast = cv2.convertScaleAbs(sepia, alpha=alpha, beta=beta)

    # Add a film grain effect to the image
    noise = np.zeros(retro.shape, np.uint8)
    cv2.randn(noise, 0, 20)
    noise = cv2.GaussianBlur(noise, (3, 3), 0)
    film_grain = cv2.add(contrast, noise)

    # Return the resulting image
    # return film_grain

    # Show the final image
    cv2.imshow('Noir Effect', film_grain)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


retro_effect('image.jpg')
