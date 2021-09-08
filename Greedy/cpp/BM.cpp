#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include "limits.h"

using namespace std;

// 时间效率O(256+m)
int* buildBC(const string& p)
{
    int* bc = new int[256];
    for(int j=0; j<256; j++)
        bc[j] = -1;
    
    int m = p.size();
    for(int j=0; j<m; j++)
        bc[p[j]] = j;
    return bc;
}

int* buildSS(const string& p)
{
    int m = p.size();
    int* ss = new int[m];
    ss[m-1] = m;
    for(int lo=m-1, hi=m-1, j=lo-1; j>=0; j--)
    {
        if((lo<j)&&(ss[m-hi+j-1]<=j-lo))
            ss[j] = ss[m-hi+j-1];
        else{
            hi = j;
            lo = min({lo, hi});
            while((0<=lo)&&(p[lo]==p[m-hi+lo-1]))
                lo--;
            ss[j] = hi - lo;
        }
    }
    return ss;
}

int* buildGS(const string& p)
{
    int* ss = buildSS(p);
    int m = p.size();
    int* gs = new int[m];
    for(int j=0; j<m; j++)
        gs[j] = m;
    for(int i=0, j=m-1; j<INT_MAX; j--)
        if(j+1 == ss[j])
            while (i<m-j-1)
                gs[i++] = m - j - 1;
    for(int j=0; j<m-1; j++)
        gs[m-ss[j]-1] = m - j - 1;
    delete [] ss;
    return gs;
            
}

// 匹配效率为O(N), 所以总的效率为O(m+n)
int KMP(const string& pat, const string& txt)
{
    int M = pat.size();
    int N = txt.size();

    int* gs = buildGS(pat);
    int* bc = buildBC(pat);
    int i = 0;
    while(i+M <= N)
    {
        int j = M - 1;
        while(pat[j] == txt[i+j])
            if(0 > --j)
                break;
        if(0 > j)
            break;
        else
            i += max({gs[j], j-bc[txt[i+j]]});
    }
    delete [] gs;
    delete [] bc;
    return i;   
}