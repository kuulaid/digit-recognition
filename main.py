#pip install -r requirements.txt

#virtualenv tf_env

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf


# mnist = tf.keras.datasets.mnist #direct loading of data

# (x_train, y_train), (x_test, y_test) = mnist.load_data()
# train = training images and labels
# test = testing images and labels

# #Normalize
# x_train = tf.keras.utils.normalize(x_train, axis=1)
# x_test = tf.keras.utils.normalize(x_test, axis=1)

# model = tf.keras.models.Sequential()
# model.add(tf.keras.layers.Flatten(input_shape = (28, 28))) #flattens into 1D Vector of 784 elements, dense requires 1D input
# model.add(tf.keras.layers.Dense(128, activation='relu'))
# model.add(tf.keras.layers.Dense(128, activation='relu'))
# model.add(tf.keras.layers.Dense(10, activation='softmax'))

# model.compile(
#     optimizer='adam',
#     loss='sparse_categorical_crossentropy', 
#     metrics=['accuracy']
# )

# model.fit(x_train, y_train, epochs=3)

# model.save('handwritten.keras')


model = tf.keras.models.load_model('handwritten.keras')

image_number = 1

while os.path.isfile(f"digits/digit{image_number}.png"):

    try:
        img = cv2.imread(f"digits/digit{image_number}.png")[:,:,0]
        img = np.invert(np.array([img]))
        prediction = model.predict(img)

        print(f"This digit is probably a {np.argmax(prediction)}")
        plt.imshow(img[0], cmap=plt.cm.binary)
        plt.show()

    except:
        print("Error!")

    finally:
        image_number += 1
    
        
