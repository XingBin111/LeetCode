#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

// 暴力方法创建, O(M^2)
vector<int> construct_table_brute(const string& pat)
{
    int M = pat.size();

    // 构造最长公共前后缀, 这是KMP算法最核心的部分
    vector<int> dp_table(M, -1);
    for(int i=1; i<M; i++)
    {
        string tmp = pat.substr(0, i);
        int j = 0;
        int res = 0;
        while(j<tmp.size()-1)
        {   
            // 从最短的公共前后缀开始校验, 可以从最长的公共前后缀开始校验, 找到了就直接break
            if(tmp.substr(0, j+1) == tmp.substr(tmp.size()-j-1, j+1))
                res = j + 1;
            j++;
        }
        dp_table[i] = res;
    }
    // for(auto& x: dp_table)
    //     cout << x << endl;
    return dp_table;
}

// 迭代创建, O(M)
vector<int> construct_table_iteration(const string& pat)
{
    int M = pat.size();

    vector<int> dp_table(M, -1);

    // t = dp_table[j]
    int t = -1;
    int j = 0;
    while(j < M - 1)
    {
        if(0 > t || pat[j] == pat[t])
        {
            j++;
            t++;
            dp_table[j] = t;
        }
        else
            t = dp_table[t];
    }
    // for(int j=1; j < M; j++)
    // {   
    //     int t = dp_table[j-1];
    //     while(t >= 0 && pat[j-1] != pat[t])
    //         t = dp_table[t];
    //     dp_table[j] = t + 1;
    // }

    for(int i=0; i<dp_table.size(); i++)
        cout << dp_table[i] << endl;
    return dp_table;
}

// 迭代创建, O(M)
vector<int> construct_table_better(const string& pat)
{
    int M = pat.size();

    vector<int> dp_table(M, -1);

    int t = -1;
    int j = 0;
    while(j < M - 1)
    {
        if(0 > t || pat[j] == pat[t])
        {
            j++;
            t++;
            dp_table[j] = (pat[j] != pat[t] ? t : dp_table[t]);
        }
        else
            t = dp_table[t];
    }

    for(int i=0; i<dp_table.size(); i++)
        cout << dp_table[i] << endl;
    return dp_table;
}

// 匹配效率为O(N), 所以总的效率为O(m+n)
int KMP(const string& pat, const string& txt)
{
    int M = pat.size();
    int N = txt.size();

    // 构造最长公共前后缀, 这是KMP算法最核心的部分
    vector<int> dp_table = construct_table_better(pat);
    
    int j = 0;
    int i = 0;
    while(j < M && i < N)
    {
        if(txt[i] == pat[j] || 0 > j)
        {
            i++;
            j++;
        }
        else
            j = dp_table[j];
    }
    return i - j;   
}

int main()
{
    string pat = "ABABC";
    // string pat = "00010";
    string txt = "CABAABABCC";
    int res = KMP(pat, txt);
    // cout << res << endl;
    // cout << txt.substr(res, pat.size()) << endl;
    return 0;
}