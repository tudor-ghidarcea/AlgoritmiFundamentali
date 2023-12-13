#include <iostream>
#include <fstream>
using namespace std;

///s = vizitare succesori. p = vizitare predecesori
int n, a[106][106], s[106], p[106];
int ctc[106], nrc;

void citire()
{
    ifstream fin("graf.in");
    fin>>n;
    int x, y;
    while(fin>>x>>y)
        a[x][y] = 1;
}

void dfs1(int x)
{
    s[x] = 1;
    for(int i=1; i<=n; i++)
        if(s[i] == 0 && a[x][i] == 1)
            dfs1(i);
}


void dfs2(int x)
{
    p[x] = 1;
    for(int i=1; i<=n; i++)
        if(p[i] == 0 && a[i][x] == 1)
            dfs2(i);
}


void algoritm()
{
    for(int i=1; i<=n; i++)
        if(ctc[i] == 0)
        {
            for(int j=1; j<=n; j++)
                s[j] = p[j] = 0;
            nrc++;
            dfs1(i);
            dfs2(i);
            for(int j=1; j<=n; j++)
                if(s[j] == 1 && p[j] == 1)
                    ctc[j] = nrc;
        }

    for(int i=1; i<=nrc; i++)
    {
        cout<<"componenta tare conexa: "<<i<<" este: ";
        for(int j=1; j<=n; j++)
            if(ctc[j] == i)
                cout<<j<<" ";
        cout<<endl;
    }

}
int main()
{
    citire();
    algoritm();
    return 0;
}
