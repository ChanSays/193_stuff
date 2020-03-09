
# MLP for Pima Indians Dataset saved to single file
from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense


# load and evaluate a saved model
from numpy import loadtxt
from keras.models import load_model
 
# load pima indians dataset
dataset = loadtxt("pima-indians-diabetes.csv", delimiter=",")
# split into input (X) and output (Y) variables
X = dataset[:,0:8]
Y = dataset[:,8]
# define model
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
# compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# Fit the model
model.fit(X, Y, epochs=150, batch_size=10, verbose=0)
# evaluate the model
scores = model.evaluate(X, Y, verbose=0)
print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
# save model and architecture to single file
model.save("model.h5")
print("Saved model to disk")

# Create a basic model instance
# model = create_model()

# Display the model's architecture
print("====================BEFORE SAVE====================\n")
model.summary()
print("============================================================\n")


model.save('my_model.h5') # creates a HDF5 file ‘my_model.h5’
del model # deletes the existing model

# returns a compiled model
# identical to the previous one
model = load_model('./my_model.h5')
# Display the model's architecture
print("====================AFTER SAVE====================\n")
model.summary()
print("============================================================\n")

# load boto3
# save boto3
# send gcp 
# 
# show training results in web
