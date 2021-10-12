import numpy as np
import keras.models
from keras import Model

model = keras.models.load_model('model_binary.hdf5')
training_data = np.array([[1 if j==i else 0 for j in range(0,32)] for i in range(0,32)], "float32")
target_data = np.array([[1 if j==i else 0 for j in range(0,32)] for i in range(0,32)], "float32")

print(model.predict(training_data).round())
scores = model.evaluate(training_data, target_data, return_dict=True)
print(scores)

extractor = Model(inputs=model.inputs, outputs=[model.layers[0].output])
features = extractor(training_data)
for i in features:
    print(list(map(round, i.numpy())))


