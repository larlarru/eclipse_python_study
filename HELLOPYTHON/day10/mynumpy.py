import numpy as np

a = [1,2,3,4,5,6,7,8]
print(a)

b = np.reshape(a, [2,4])
b = b + 1
print(b)

c = [
        [1,2,3,4],
        [5,6,7,8]
    ]

print(c[1][2])
# print(c[1,2]) 2차원 배열은 이렇게 하면 오류난다.

print(b[1][2])
print(b[1, 2])


