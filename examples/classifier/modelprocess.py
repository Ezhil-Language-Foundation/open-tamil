# (C) 2017 Muthiah Annamalai
# This file is part of open-tamil examples
# This code is released under public domain

import numpy as np
import random
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

def data1(filename):
    x = np.loadtxt(open(filename,"r"),delimiter=",")
    y = np.ones(shape=(x.size,1))
    return (x,y)

def data0(filename):
    x = np.loadtxt(open(filename,"r"),delimiter=",")
    y = np.zeros(shape=(x.size,1))
    return (x,y)

DEBUG = False
N = 10000  #training set

ta_x1,ta_y1 = data1("tamilvu_dictionary_words.txt.csv")
x1 = ta_x1.copy()
y1 = ta_y1.copy()

## mix these rows and pick N
jf_x0,jf_y0 = data0("english_dictionary_words.jaffna.csv")
x0 = jf_x0.copy()
y0 = jf_y0.copy()

az_x0,az_y0 = data0("english_dictionary_words.azhagi.csv")
cm_x0,cm_y0 = data0("english_dictionary_words.combinational.csv")

## Pick N items
# we don't bother with collisions in random.choice which should be rare
randrows = [random.choice(range(0,x0.shape[0])) for i in range(0,N)]
x0 = x0.take(randrows,axis=0)
y0 = y0.take(randrows,axis=0)

validaterows = []
for i in range(0,jf_x0.shape[0]):
    if not ( i in randrows) and i < x0.shape[0]:
        validaterows.append(i)

validate_x0 = x0.take(validaterows,axis=0)
validate_y0 = np.zeros(shape=(len(validaterows),1))

x1 = x1.take(randrows,axis=0)
y1 = y1.take(randrows,axis=0)

validate_x1 = x1.take(validaterows,axis=0)
validate_y1 = np.ones(shape=(len(validaterows),1))

## Mixup N items with other English Transliteraiton data sets
for i in range(0,int(N/5)):
    choice_src = random.choice(range(0,az_x0.shape[0]))
    choice_des = random.choice(range(0,x0.shape[0]))
    if DEBUG:
        print(az_x0[choice_src])
        print(x0[choice_des])
    for idx,val in enumerate(az_x0[choice_src]):
        x0[choice_des,idx] = val
    choice_src = random.choice(range(0,cm_x0.shape[0]))
    choice_des = random.choice(range(0,x0.shape[0]))
    for idx,val in enumerate(cm_x0[choice_src]):
        x0[choice_des,idx] = val

if DEBUG:
    print(x0)
    print(x1)

###########
## Build training set for the model
nn = MLPClassifier(solver='sgd',alpha=1e-5,activation='logistic',hidden_layer_sizes=(100,50,10,1),random_state=1,max_iter=10000)
X = np.concatenate((x0,x1),axis=0)
Y = np.concatenate((y0,y1),axis=0)
Y = Y.ravel()
print(X)
print(Y)
nn.fit(X,Y)
validate_X = validate_x1.copy()
validate_Y = validate_y1.copy()
validate_X.resize((validate_X.shape[0]+validate_x0.shape[0],validate_x0.shape[1]))
validate_Y.resize((validate_Y.shape[0]+validate_y0.shape[0],validate_y0.shape[1]))
for idx in range(validate_X.shape[0],validate_X.shape[0]):
    for idcol in range(0,validate_X.shape[1]):
        validate_X[idx,idcol] = validate_x0[idx-validate_X.shape[0],idcol]
    validate_Y[idx,0] = validate_y0[idx-validate_X.shape[0],0]
    
y_valid = nn.predict(validate_X)
print(" accuracy => ",accuracy_score(y_valid.ravel(),validate_Y.ravel()))
score = nn.score( validate_X, validate_Y.ravel() )
print("Score => ")
print(score)
