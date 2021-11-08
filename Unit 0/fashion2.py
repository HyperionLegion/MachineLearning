import tensorflow as tf
import numpy as np
import keras.models
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from tensorflow.keras.utils import plot_model

#fashion_mnist = tf.keras.datasets.fashion_mnist

# load and prepare the image
def load_image(filename):
	# load the image
	img = load_img(filename, color_mode="grayscale", target_size=(28, 28))
	# convert to array
	img = img_to_array(img)
	# reshape into a single sample with 1 channel
	img = img.reshape(1, 28, 28, 1)
	# prepare pixel data
	img = img.astype('float32')
	img = img / 255.0
	return img

img = load_image('sandal.jpg')

#(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

model = keras.models.load_model('model_fashion.hdf5')
plot_model( model , to_file = 'fashion.png' , show_shapes = True )

probability_model = tf.keras.Sequential([model, 
                                         tf.keras.layers.Softmax()])
#predictions = probability_model.predict(test_images)
predictions = probability_model.predict(img)
print(predictions[0])
print(np.argmax(predictions[0]))
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
print(class_names[np.argmax(predictions[0])])