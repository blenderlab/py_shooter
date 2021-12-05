import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import numpy as np
import csv


# load the dataset
x_train=[]
y_train=[]
x_test=[]
y_test=[]

file = open("py_shooter_data.csv","r")
csvReader = csv.reader(file)
for row  in csvReader :
    x_train.append([int(row[0]),int(row[1]),int(row[2]),int(row[3])])        
    y_train.append([int(row[4])])
                   
x_test = x_train[0:100]
y_test = y_train[0:100]                       

#2 create the model :

model = keras.models.Sequential()
model.add(keras.layers.Flatten(input_shape=(4,)))
model.add(keras.layers.Dense(6, activation="relu"))
model.add(keras.layers.Dense(4, activation="softmax"))

model.compile(loss="sparse_categorical_crossentropy",
              optimizer="adam",
              metrics=["accuracy"])

#print model summary 
model.summary()

# 3 Train it!
model_history = model.fit(x_train,y_train,batch_size=50,epochs=10,validation_data=(x_test,y_test))

model.evaluate(x_test,y_test,batch_size=1)

model.save("py_shooter.h5")
