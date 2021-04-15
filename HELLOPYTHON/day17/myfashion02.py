import tensorflow as tf
import cv2

fashion_mnist = tf.keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

for i in range(len(train_labels)):
    label = str(train_labels[i])
    cv2.imwrite("image/"+label+"_"+str(i)+".jpg", train_images[i])

cv2.waitKey(0)
cv2.destroyAllWindows()

# class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
#                'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
# 
# train_images = train_images / 255.0
# test_images = test_images / 255.0
# 
# model = tf.keras.Sequential([
#     tf.keras.layers.Flatten(input_shape=(28, 28)),
#     tf.keras.layers.Dense(128, activation='relu'),
#     tf.keras.layers.Dense(10, activation='softmax')
# ])
# 
# model.compile(optimizer='adam',
#               loss='sparse_categorical_crossentropy',
#               metrics=['accuracy'])
# 
# model.fit(train_images, train_labels, epochs=10)
# 
# 
# test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)
# print('\nTest accuracy:', test_acc)