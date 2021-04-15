from cv2 import cv2

# 1.2.jpg

img = cv2.imread('HQ66W2S.jpg', 1)

cv2.imshow('Test Image', img)
cv2.imwrite('test2.jpg', img)
cv2.waitKey(0)

cv2.destroyAllWindows()