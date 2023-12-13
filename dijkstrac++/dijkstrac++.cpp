#include <iostream>
#include <fstream>
#define inf 100000000
using namespace std;

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
void afisare()
{
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=n;j++)
            cout<<a[i][j]<<" ";
        cout<<endl;
    }
}
int main()
{
    citire();
    afisare();
    return 0;
}
