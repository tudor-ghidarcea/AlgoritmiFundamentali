///Roy_Floyd
///calculeaza drumul minim
///de la oricare nod la oricare nod

#include <iostream>
#include <fstream>
using namespace std;

int const inf = 1234567;

int n, a[101][101];
ifstream fin("graf.in");

void citire()
{
     fin>>n;
    int x, y, c;
    while(fin>>x>>y>>c)
        a[x][y] = c;
    for(int i=1;i<=n;i++)
        for(int j=1;j<=n;j++)
            if(i!= j && a[i][j] == 0)
                a[i][j] = inf;
}

void Roy_Warshall()
{
    for(int k=1;k<=n;k++)///nod intermediar
        for(int i=1;i<=n;i++)///sursa
            for(int j=1;j<=n;j++)///destinatia
                if(a[i][k] + a[k][j] < a[i][j])
                    a[i][j] = a[i][k] + a[k][j];
}
void afisare()
{
    cout<<"costul drumurilor minime intre noduri:"<<endl;
    for(int i=1;i<=n;i++)
        for(int j=1;j<=n;j++)
            if(a[i][j] < inf && i != j)
                cout<<i<<" - "<<j<<" - "<<a[i][j]<<endl;

}
int main()
{
    citire();
    Roy_Warshall();
    afisare();
    return 0;
}
