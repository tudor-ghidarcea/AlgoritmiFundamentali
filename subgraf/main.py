'''
Cerinţa
Se dă lista muchiilor unui graf neorientat cu n vârfuri,
 etichetate de la 1 la n. Din acest graf se elimină toate
  vârfurile etichetate cu valori prime. Să se determine câte muchii va avea subgraful obținut.

Date de intrare
Fişierul de intrare subgraf.in conţine pe prima linie numărul n,
 reprezentând numărul de vârfuri ale grafului.
  Fiecare dintre următoarele linii conține câte o
  pereche de numere i j, cu semnificația că există muchie între i și j.

Date de ieşire
Fişierul de ieşire subgraf.out va conţine pe prima linie numărul M de muchii ale subgrafului obținut.
'''
f = open("subgraf1.in","r")
lines = f.readlines()
nr=int(lines[0].split()[0])
matrice_adiacenta = []
def prim(x):
    if x > 1:

        for i in range(2, int(x / 2) + 1):

            if (x % i) == 0:
                return 0
                break
        else:
            return 1

    else:
        return 0
for i in range(nr):
    line = []
    for i in range(nr):
        line.append('0')
    matrice_adiacenta.append(line)
for line in lines[1:]:
    x=int(line[0])-1
    y=int(line[2])-1
    if prim(x)==0 and prim(y)==0:
        matrice_adiacenta[x][y]=1
#suma gradelor nodurilor este dublul numarului de muchii
suma_grade=0
def get_grad(x):
    g = 0
    for i in range(nr):
        g=g+int(matrice_adiacenta[x][i])
    return g
for i in range(nr):
    suma_grade+=get_grad(i)

print("Numarul de muchii este "+str(int(suma_grade/2)))
