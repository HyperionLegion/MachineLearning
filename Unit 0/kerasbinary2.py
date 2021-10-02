import numpy as np
import keras.models
from keras.models import Sequential
from keras.layers.core import Dense

model = keras.models.load_model('model_binary.hdf5')
training_data = np.array([[1 if j==i else 0 for j in range(0,32)] for i in range(0,32)], "float32")
target_data = np.array([[1 if j==i else 0 for j in range(0,32)] for i in range(0,32)], "float32")

print(model.predict(training_data).round())
scores = model.evaluate(training_data, target_data, return_dict=True)
print(scores)
