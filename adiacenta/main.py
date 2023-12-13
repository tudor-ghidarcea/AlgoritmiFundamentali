#adiacenta
#programul citeste din fisier muchiile unui graf si
#returneaza intr-un fisier de iesire matricea de adiacenta
f = open("adiacenta.in","r")
lines = f.readlines()
h=int(lines[0].split()[0])
w=h
matrice_adiacenta = []
for i in range(h):
    line = []
    for i in range(h):
        line.append('0')
    matrice_adiacenta.append(line)
for line in lines[1:]:
    x=int(line[0])-1
    print(x)
    y=int(line[2])-1
    print(y)
    matrice_adiacenta[x][y]=1

print(matrice_adiacenta)

out=open("adiacenta.out","w")
out.write(str(matrice_adiacenta))