import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
from mpl_toolkits.mplot3d import Axes3D
import tensorflow as tf
import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.models import Model, Input
from keras.callbacks import TensorBoard
from model_data_service import ModelDataService

print('tensorflow_version: ', tf.__version__)
print('keras_version: ', keras.__version__)

model_data_service = ModelDataService()
data = model_data_service.get_ticker_df('KMX')
data.head()

data.describe()

figure = plt.figure()
ax = Axes3D(figure)
ax.scatter(data['x1'], data['x2'], data['y'], c = 'blue', marker = 'o', alpha = 0.5)
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('y')
ax.set_title('KMX data')
plt.show()

feature_names = ['x1', 'x2']
data_x = data[feature_names]
data_y = data['y']
print('input shape: ', data_x.shape)
print('output_shape: ', data_y.shape)
data_x1 = data['x1']
data_x2 = data['x2']
print('number of samples: ', data_x1.shape)

# Reshape data.
data_x = np.array(data_x)
data_y = np.array(data_y)

figure = plt.figure()
ax = Axes3D(figure)
ax.scatter(data_x1, data_x2, data_y, c = 'blue', marker = 'o', alpha = 0.5)
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('y')
ax.set_title('Normalized KMX data')
plt.show()

# Model definition.
model = Sequential()
model.add(Dense(1, input_dim = 2, init = 'normal', activation = 'relu'))

# Compile model.
model.compile(loss='mean_squared_error', optimizer='adam', metrics=['mse'])

model.summary()

tensorboard = TensorBoard(log_dir = './keras_logs_smt_regression')

# Train model.
hist = model.fit(data_x, data_y, batch_size = 1, epochs = 2100, shuffle = False, callbacks = [tensorboard])

# Graphically display loss and accuracy
num_epochs = 2100
train_loss = hist.history['loss']
xc = range(num_epochs)

plt.figure(1, figsize = (7, 5))
plt.plot(xc, train_loss)
plt.xlabel('loss')
plt.ylabel('epoch')
plt.title('train_loss')
plt.grid(True)
plt.legend(['train', 'val'])
plt.style.use(['classic'])

x_test = np.array(data_x[0:20])
y_test = np.array(data_y[0:20])
score = model.evaluate(x_test, y_test)
print('Test loss: ', score[0])

x_test = np.array(data_x[0:5])
y_test = np.array(data_y[0:5])
y_test_predicted = model.predict(x_test)
print('Predicted value:\n', y_test_predicted)
print('Actual value:\n', y_test)

# Obtain trained weights.
params = model.layers[0].get_weights()
w = params[0]
b = params[1]
print('Weights: ', w)
print('bias: ', b)

# Plot trained model.
x1_surface, x2_surface = np.meshgrid(np.linspace(data_x1.min(),data_x1.max(),100), np.linspace(data_x2.min(),data_x2.max(),100))
y_predicted_surface = x1_surface * w[0] + x2_surface * w[1] + b
figure = plt.figure()
ax = Axes3D(figure)
sct = ax.scatter(data_x1, data_x2, data_y, c = 'blue', marker = 'o', alpha = 0.5)
plt_surface = ax.plot_surface(x1_surface, x2_surface, y_predicted_surface, edgecolors='r', alpha = .2)
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('y')
ax.set_title('KMX Linear Regression results')
plt.legend(['data_x, data_y'], bbox_to_anchor = (1, 0.8), loc = 4)
plt.show()

# Save trained model.
model.save('smt-regression-model.h5')

from tensorflow.keras.models import load_model
smt_model = load_model('smt-regression-model.h5')
smt_model.get_weights()
weights = smt_model.get_weights()

print('P/E value: ', weights[0][0])
print('g coefficient: ', weights[0][1])
print('bias: ', weights[1][0])

data = model_data_service.get_ticker_df('GOOGL')
data_x_GOOGL = data[feature_names]
data_x_GOOGL = np.array(data_x_GOOGL)

data_y_GOOGL = data['y']
data_y_GOOGL = np.array(data_y_GOOGL)

y_GOOGL_predicted = model.predict(data_x_GOOGL)


data_x1_GOOGL = data['x1']
data_x2_GOOGL = data['x2']

# Train further against GOOGL data
hist = model.fit(data_x_GOOGL, data_y_GOOGL, batch_size = 1, epochs = 2100, shuffle = False, callbacks = [tensorboard])

# Graphically display loss and accuracy
num_epochs = 2100
train_loss = hist.history['loss']
xc = range(num_epochs)

plt.figure(1, figsize = (7, 5))
plt.plot(xc, train_loss)
plt.xlabel('loss')
plt.ylabel('epoch')
plt.title('train_loss')
plt.grid(True)
plt.legend(['train', 'val'])
plt.style.use(['classic'])

# Plot trained model.
x1_surface, x2_surface = np.meshgrid(np.linspace(data_x1_GOOGL.min(),data_x1_GOOGL.max(),100), np.linspace(data_x2_GOOGL.min(),data_x2_GOOGL.max(),100))
y_predicted_surface = x1_surface * w[0] + x2_surface * w[1] + b
figure = plt.figure()
ax = Axes3D(figure)
sct = ax.scatter(data_x1_GOOGL, data_x2_GOOGL, data_y_GOOGL, c = 'blue', marker = 'o', alpha = 0.5)
plt_surface = ax.plot_surface(x1_surface, x2_surface, y_predicted_surface, edgecolors='r', alpha = .2)
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('y')
ax.set_title('KMX + GOOGL Linear Regression results')
plt.legend(['data_x, data_y'], bbox_to_anchor = (1, 0.8), loc = 4)
plt.show()