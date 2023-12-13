'''
Cerinţa
Se dă lista muchiilor unui graf neorientat cu n vârfuri, etichetate de la 1 la n
și un număr natural k. Din acest graf se elimină toate muchiile care au
ambele extremități în vârfuri de grad mai mare sau egal cu k. Să se afișeze matricea de adiacență a grafului parțial obținut.

Date de intrare
Fişierul de intrare graf_partial_5.in conţine pe prima linie numărul n, reprezentând numărul
 de vârfuri ale grafului și numărul k. Fiecare dintre următoarele linii conține câte o pereche
  de numere i j, cu semnificația că există muchie între i și j.

Date de ieşire
Fişierul de ieşire graf_partial_5.out va conţine matricea de adiacență a grafului
parțial obținut, câte o linie a matricei pe o linie a fișierului, elementele de pe fiecare linie fiind separate prin exact un spațiu.
'''

f = open("graf_partial_5.in","r")
lines = f.readlines()
aux=[]
aux.append(lines[0])
nr=int(lines[0].split()[0])
k=int(lines[0].split()[1])
for line in lines:
    if (int(line[0])<k and int(line[2])<k):
        aux.append(line)


matrice_adiacenta = []
for i in range(nr):
    line = []
    for i in range(nr):
        line.append('0')
    matrice_adiacenta.append(line)
for line in lines[1:]:
    x=int(line[0])-1
    print(x)
    y=int(line[2])-1
    print(y)
    matrice_adiacenta[x][y]=1
iesire=open("graf_partial_5.out", "w")
iesire.write(str(matrice_adiacenta))