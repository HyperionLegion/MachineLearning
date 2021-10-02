import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense

# the four different states of the XOR gate
training_data = np.array([[0,0],[0,1],[1,0],[1,1]], "float32")

# the four expected results in the same order
target_data = np.array([[0],[1],[1],[0]], "float32")

model = Sequential()
model.add(Dense(3, input_dim=2, activation='sigmoid'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['binary_accuracy'])

model.fit(training_data, target_data, epochs=10000, verbose=2)

scores = model.evaluate(training_data, target_data)
print(model.metrics_names[1]*100)

print(model.predict(training_data))

for layer in model.layers:
    weights = layer.get_weights() # list of numpy arrays
    arr = [i.tolist() for i in weights]
    print(arr)
    #[[[x1s], [x2s]],[bias]]