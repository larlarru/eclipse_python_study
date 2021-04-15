import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

# make 3d axes
fig = plt.figure()
ax = fig.gca(projection='3d')

# test data
x = np.array([0,1,2,3,4])
y = np.array([0,1,2,3,4])
# x = np.arange(-1., 1., .1)
# y = np.arange(-1., 1., .1)
z1 = np.array([2,1,8,3,7])
# z2 = np.array([0,1,2,3,4])
# z3 = np.array([6,0,9,1,5])
# z1 = x + y
# z2 = x * x
# z3 = -y * y

# plot test data
ax.plot(x, y, z1)
ax.plot(x+1, y, z1)
ax.plot(x+2, y, z1)
# ax.plot(x, y, z2)
# ax.plot(x, y, z3)

# make labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

print("x :",x)
print("y :",y)
print("z1 :",z1)
# print("z2 :",z2)
# print("z3 :",z3)

plt.show()

