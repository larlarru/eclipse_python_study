from cv2 import cv2

img = cv2.imread('rgb.png')

print(img)

img[0][0][0] = 255
img[0][0][1] = 0
img[0][0][2] = 0

img[0][1][0] = 255
img[0][1][1] = 0
img[0][1][2] = 0

img[1][0][0] = 255
img[1][0][1] = 0
img[1][0][2] = 0

img[1][1][0] = 255
img[1][1][1] = 0
img[1][1][2] = 0


print("shape : ", img.shape)

cv2.imshow('Test Image', img)
cv2.waitKey(0)

cv2.destroyAllWindows()