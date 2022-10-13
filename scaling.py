import cv2
import numpy as np

FILE_NAME = "dog.jpeg"

try:
    # Read image from disk
    img = cv2.imread(FILE_NAME)

    # Get number of pixel horizontally and vertically.
    (height, width) = img.shape[:2]

    # Specify the size of image along with interpolation methods.
    # cv2.INTER_AREA is used for shrinking, whereas cv2.INTER_CUBIC
    # is used for zooming

    res = cv2.resize(img, (int(width / 2), int(height / 2)), interpolation = cv2.INTER_CUBIC)

    # Write image back to disc
    cv2.imwrite("result.jpg", res)
except IOError:
    print("Error while reading files !!!")

cv2.imshow("newImage", res)
cv2.waitKey(0)
cv2.destroyAllWindows()