///determina drumul de la nodul sursa la celelalte noduri
#include <fstream>
#include <iostream>
using namespace std;
#define inf 100000

int n, a[101][101];
int tata[101], d[101], viz[101], start;
ifstream fin("graf.in");

void citire()
{
    fin>>n>>start;
    int x, y, c;
    while(fin>>x>>y>>c)
        a[x][y] = c;
    for(int i=1;i<=n;i++)
        for(int j=1;j<=n;j++)
            if(a[i][j] == 0 && i != j)
                a[i][j] = inf;
}

void initializare()
{
    for(int i=1;i<=n;i++)
    {
        d[i] = a[start][i];///distanta de la sursa la nodul i
        tata[i] = start;///tatal nodului i
    }
    tata[start] = 0;///tatal sursei - n-are
    viz[start] = 1;///am trecut prin sursa
}

void Dijkstra()
{
    for(int k=1;k<=n-1;k++)
    {
        ///caut cel mai apropiat nod de start
        int dmin = inf, vfmin;
        for(int i=1;i<=n;i++)
            if(viz[i] == 0 && dmin > d[i]) ///21, 3, 5
            {
                dmin = d[i];///3
                vfmin = i;///3
            }
        ///selecatre varf minim
        viz[vfmin] = 1;
        ///recalculez distanta de la sursa la celelalte noduri
        ///tinand cont de dmin
        for(int i=1;i<=n;i++)
            if(viz[i] == 0 && d[i] > dmin + a[vfmin][i])
            {
                tata[i] = vfmin;
                d[i] = dmin + a[vfmin][i];
            }
    }
}

///sursa = 1, destinatia = 4
void afisare_drum(int destinatia, int sursa)
{
    if(destinatia == sursa)
    {
       cout<<sursa<<" ";
       return;
    }

    afisare_drum(tata[destinatia], sursa);
    cout<<destinatia<<" ";
}

void afisare()
{
    cout<<"distantele: ";
    for(int i=1;i<=n;i++)
        cout<<d[i]<<" ";

    cout<<endl<<endl;
    cout<<"tatii:";
    for(int i=1;i<=n;i++)
        cout<<tata[i]<<" ";
}
int main()
{
    citire();
    initializare();
    Dijkstra();
    afisare();
    cout<<endl;
    int sursa, destinatie;
    cout<<"destinatie = ";
    cin>>destinatie;
    cout<<"sursa = ";
    cin>>sursa;
    afisare_drum(destinatie, sursa);
    return 0;
}
