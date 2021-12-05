from tensorflow import keras
import numpy as np
import csv
from  settings import * 


# load the dataset
x_train=[]
y_train=[]
x_test=[]
y_test=[]

file = open(FILENAME,"r")
csvReader = csv.reader(file)
for row  in csvReader :
    x_train.append([int(row[0]),int(row[1]),int(row[2]),int(row[3])])        
    y_train.append([int(row[4])])
                   
x_test = x_train[0:100]
y_test = y_train[0:100]                       

print (x_test[0:10])
print (y_test[0:10])

#2 create the model :

model = keras.models.Sequential()

# We have 4 inputs : Xpositiont, Left ennemies, Center Ennemies, Right Ennemies
model.add(keras.layers.Dense(units=4,input_shape=(4,1),input_dim=1))

# Adding 8 nerons hidden layer
model.add(keras.layers.Dense(6,activation="relu"))
model.add(keras.layers.Dense(4,activation="relu"))
model.add(keras.layers.Dense(4,activation="relu"))

# OUtput with a single output  : Action 
model.add(keras.layers.Dense(1,activation="sigmoid"))

# 3 Train it!

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy']) 

#print model summary 
model.summary()

# 3 Train it!
model_history = model.fit(x_train,y_train,batch_size=10,epochs=10,validation_data=(x_test,y_test))
# Check model efficiency : 
model.evaluate(x_test,y_test,batch_size=100)
print(model.predict(x_test[0:1]))

# save it : 
model.save(MODELNAME)
