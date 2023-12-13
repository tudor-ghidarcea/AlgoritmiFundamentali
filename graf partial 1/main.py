'''Cerinţa
Se dă lista muchiilor unui graf neorientat cu n vârfuri, etichetate de la 1 la n.
 Din acest graf se elimină toate muchiile cu o extremitate de grad maxim și cealaltă extremitate de grad minim.
  Să se determine numărul de muchii eliminate și să se afișeze matricea de adiacență a grafului parțial obținut.

Date de intrare
Fişierul de intrare graf_partial_1.in conţine pe prima linie numărul n, reprezentând numărul de vârfuri ale grafului.
Fiecare dintre următoarele linii conține câte o pereche de numere i j, cu semnificația că există muchie între i și j.

Date de ieşire
Fişierul de ieşire graf_partial_1.out va conţine pe prime linie numărul de muchii eliminate,
iar pe următoarele linii matricea de adiacență a grafului parțial obținut,
câte o linie a matricei pe o linie a fișierului, elementele de pe fiecare linie fiind separate prin exact un spațiu.
'''


f = open("graf_partial_1.in","r")
lines = f.readlines()
aux=[]
nr=int(lines[0].split()[0])
grad_maxim=0
grad_minim=100
for linie in lines[1:]:
    if int(linie[0])>grad_maxim:
        grad_maxim=int(linie[0])
    if int(linie[0])<grad_minim :
        grad_minim=int(linie[0])
    if int(linie[2])>grad_maxim:
        grad_maxim=int(linie[2])
    if  int(linie[2])<grad_minim:
        grad_minim=int(linie[2])
muchii_eliminate=0

for line in lines[1:]:
    if (int(line[0])==grad_maxim and int(line[2])==grad_minim):
        muchii_eliminate+=1
    elif (int(line[0])==grad_minim and int(line[2])==grad_maxim):
        muchii_eliminate+=1

for line in lines[1:]:
    if (int(line[0])!=grad_maxim and int(line[2])!=grad_minim):
        aux.append(line)
    elif (int(line[0])!=grad_minim and int(line[2])!=grad_maxim):
        aux.append(line)

matrice_adiacenta = []
for i in range(nr):
    line = []
    for i in range(nr):
        line.append('0')
    matrice_adiacenta.append(line)
for line in aux:
    x=int(line[0])-1
    y=int(line[2])-1
    matrice_adiacenta[x][y]=1


iesire=open("graf_partial_1.out", "w")
iesire.write(str(muchii_eliminate)+"\n"+str(matrice_adiacenta))
