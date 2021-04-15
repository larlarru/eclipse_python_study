from cv2 import cv2

img = cv2.imread('HQ66W2S.jpg')
img_rotate_90_clockwise = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

print(img)
print("shape : ", img.shape)

for i in img:
    for j in i:
        j[1] = 0
        j[2] = 0

cv2.imshow('Test Image', img_rotate_90_clockwise)
cv2.waitKey(0)

cv2.destroyAllWindows()