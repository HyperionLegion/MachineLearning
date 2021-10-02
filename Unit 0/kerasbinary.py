import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense

training_data = np.array([[1 if j==i else 0 for j in range(0,32)] for i in range(0,32)], "float32")

target_data = np.array([[1 if j==i else 0 for j in range(0,32)] for i in range(0,32)], "float32")
print(training_data)
print(target_data)

model = Sequential()
model.add(Dense(5, input_dim=32, activation='sigmoid'))
model.add(Dense(32, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['binary_accuracy'])

model.fit(training_data, target_data, epochs=20000, verbose=2)

scores = model.evaluate(training_data, target_data)
#print(model.metrics_names[1]*100)

print(model.predict(training_data).round())

model.save('model_binary.hdf5')

# for layer in model.layers:
#     weights = layer.get_weights() # list of numpy arrays
#     arr = [i.tolist() for i in weights]
#     print(arr)
#     #[[[x1s], [x2s]],[bias]]