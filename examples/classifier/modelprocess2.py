# -*- coding: utf-8 -*-
# (C) 2017 Muthiah Annamalai
# This file is part of open-tamil examples
# This code is released under public domain

# Ref API help from : https://scikit-learn.org
import numpy as np
import random
import string
import time

from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.externals import joblib

# project modules
from classifier_eng_vs_ta import jaffna_transliterate
from preprocess import Feature

def data1(filename):
    x = np.loadtxt(open(filename,"r"),delimiter=",")
    y = np.ones(shape=(x.shape[0],1))
    return (x,y)

def data0(filename):
    x = np.loadtxt(open(filename,"r"),delimiter=",")
    y = np.zeros(shape=(x.shape[0],1))
    return (x,y)

DEBUG = False

x1,y1 = data1("tamilvu_dictionary_words.txt.csv")
x0,y0 = data0("english_dictionary_words.jaffna.csv")
az_x0,az_y0 = data0("english_dictionary_words.azhagi.csv")
cm_x0,cm_y0 = data0("english_dictionary_words.combinational.csv")

x1 = x1.take(range(0,x0.shape[0]),axis=0)
y1 = np.ones((x0.shape[0],1))
##  Scale the data for the training
X = np.concatenate((x0,x1),axis=0)
Y = np.concatenate((y0,y1),axis=0)
#Y = Y.take(range(0,X.shape[0]),axis=0).ravel()
Y = Y.ravel()

X_train, X_test, Y_train, Y_test = train_test_split(X,Y)
scaler = StandardScaler()
scaler.fit(X_train)

print("Size of Training set => %d"%X_train.shape[0])
print("Size of Test set => %d"%X_test.shape[0])

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

###########
## Build training set for the model
## solver='sgd',activation='logistic',
## We have a 4-layer model
#nn = MLPClassifier(hidden_layer_sizes=(15,15,10,5),
#                   max_iter=100000,alpha=0.01,solver='lbfgs')
# Try 1-layer simple model with logistic activation
nn = MLPClassifier(hidden_layer_sizes=(8,8,7),solver='lbfgs')#activation='logistic',max_iter=1000,early_stopping=True,solver='lbfgs')
#                   max_iter=500,solver='sgd',activation='logistic')
print(nn)
nn.fit(X_train,Y_train)
joblib.dump(nn,'nn-%s.pkl'%time.ctime())

Y_pred = nn.predict(X_test)
print(" accuracy => ",accuracy_score(Y_pred.ravel(),Y_test))
score = nn.score( X_test, Y_test )
print("Score => ")
print(score)

print(confusion_matrix(Y_test,Y_pred.ravel()))
print(classification_report(Y_test,Y_pred.ravel()))

def process_word(s):
    if any( [l in string.ascii_lowercase for l in s] ):
        s = jaffna_transliterate(s)
        print(u"Transliterated to %s"%s)
    print(u"Checking in NN '%s'"%s)
    try:
        f = Feature.get(s)
        scaled_feature = scaler.transform( np.array( f.data() ).reshape(1,-1)  )
        y = nn.predict(scaled_feature )
        print( scaled_feature )
        print( y )
        if y.ravel() > 0:
            print(u"%s -> TAMIL world (most likely)"%s)
        else:
            print(u"%s -> ENG word (most likely)"%s) 
    except Exception as ioe:
        print("SKIPPING => ",ioe.message)
        
    return

for w in [u"hello",u"ஆரொன்",u"உகந்த", u"கம்புயுடர்",u"கம்ப்யூட்டர்",u"பியூடிபுல்","pupil","beautiful","summer","sinful",
          "google","facebook","microsoft","swift"]:
    process_word(w)

while True:
    s = raw_input(u">> ").decode("utf-8")
    s = s.strip().lower()
    if ( s == "end" ):
        break;
    if len(s) < 1:
        continue
    process_word(s)
