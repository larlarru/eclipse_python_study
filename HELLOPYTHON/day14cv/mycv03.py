from cv2 import cv2

img = cv2.imread('1.jpg', cv2.IMREAD_GRAYSCALE)

cv2.imshow('Test Image', img)
cv2.waitKey(0)

cv2.destroyAllWindows()