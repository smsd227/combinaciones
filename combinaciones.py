import numpy as np
from sklearn import preprocessing
from sklearn.cluster import KMeans

def distancia(a,b):
    d = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            d = d + 1
    return d

def generador(nivel):
    if nivel < len(quiniela):
        for i in range(len(quiniela[nivel])):
            cActual[nivel] = quiniela[nivel][i]
            generador(nivel + 1)
    else:
        comb.append(codificador1X2.transform(cActual[:]))

quiniela = ['1X', '1', 'X2','1X', '12']
cActual = []
for i in range(len(quiniela)):
    cActual.append('')
comb = []
codificador1X2 = preprocessing.LabelEncoder()
codificador1X2.fit(["1","X","2"])
generador(0)
combinaciones = np.array(comb)
classifier = KNeighborsClassifier(n_neighbors=2,algorithm='brute',metric='hamming')
classifier.fit(combinaciones)

print(combinaciones)
