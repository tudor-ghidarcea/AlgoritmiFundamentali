'''Cerinţa
Se dă lista muchiilor unui graf neorientat cu n vârfuri, etichetate de la 1 la n. Din acest graf se elimină
toate vârfurile care au gradul minim. Să se determine câte muchii va avea subgraful obținut.

Date de intrare
Fişierul de intrare subgraf1.in conţine pe prima linie numărul n, reprezentând numărul de vârfuri ale grafului..
Fiecare dintre următoarele linii conține câte o pereche de numere i j, cu semnificația că există muchie între i și j.

Date de ieşire
Fişierul de ieşire subgraf1.out va conţine pe prima linie numărul M de muchii ale subgrafului obținut.'''
import numpy as np
from scipy.sparse import csr_matrix
f = open("subgraf1.in","r")
lines = f.readlines()
nr=int(lines[0].split()[0])
matrice_adiacenta = []
for i in range(nr):
    line = []
    for i in range(nr):
        line.append('0')
    matrice_adiacenta.append(line)
for line in lines[1:]:
    x=int(line[0])-1
    y=int(line[2])-1
    matrice_adiacenta[x][y]=1

grade=[]


def get_grad(x):
    g = 0
    for i in range(nr):
        g=g+int(matrice_adiacenta[x][i])
    return g

for i in range(nr):
    grade.append(get_grad(i))

grade.sort()
numar_muchii=0
for i in range(nr):
    if get_grad(i)>grade[0]:
        numar_muchii=numar_muchii+get_grad(i)

print(numar_muchii)
iesire = open("subgraf1.out","w")
iesire.write(str(numar_muchii))