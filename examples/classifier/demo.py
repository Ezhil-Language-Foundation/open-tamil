import sklearn
from sklearn.neural_network import MLPClassifier
X=[[0,1],[1,0],[1,1]]
Y=[1,1,0]
clf=MLPClassifier(solver='lbfgs',alpha=1e-3,hidden_layer_sizes=(5,2),random_state=1)
clf.fit(X,Y)
clf.predict([[2,2],[0,0],[-1,-2]])
print(clf.score([[2,2],[0,0],[-1,-2]],[1,0,0]))
for coef in clf.coefs_:
    print(coef)

