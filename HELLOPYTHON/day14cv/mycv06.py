from cv2 import cv2

img = cv2.imread('bts.jpg')

print(img)
print("shape : ", img.shape)

for i in img:
    for j in i:
        j[1] = 0
        j[2] = 0

cv2.imshow('Test Image', img)
cv2.waitKey(0)

cv2.destroyAllWindows()