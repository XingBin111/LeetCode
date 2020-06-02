#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <unordered_map>

using namespace std;

bool myfunction (vector<int> i,vector<int> j) { return (i[1]<j[1]); }

int interval_schedule_while(const vector<vector<int> >& intvs)
{
    int res = 0;
    int start = 0;
    int n = intvs.size();
    while(start < n)
    {   
        int jump = 0;
        for(int i=start; i<n;i++)
        {   
            // 如果i的开始时间小于start的结束时间, 即冲突
            if(intvs[i][0] < intvs[start][1])
                jump++;
        }  
        res++;
        start += jump;
    }
    return res;
}

int interval_schedule_for(const vector<vector<int> >& intvs)
{
    int res = 1;
    int x_end = intvs[0][1];
    int n = intvs.size();
    for(int i=1; i<n; i++)
    {
        if(intvs[i][0] >= x_end)
        {
            res++;
            x_end = intvs[i][1];
        }
    }
    return res;
}


int main()
{
    vector<vector<int> > intvs = {{1, 2}, {2, 3}, {3, 4}, {1, 3}};
    // sort(intvs.begin(), intvs.end(), myfunction);
    // for(int i=0; i<intvs.size(); i++)
    //     cout << intvs[i][1] << endl;
    cout << interval_schedule_for(intvs) << endl;
    return 0;
}