#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <unordered_map>

using namespace std;

int KMP(const string& pat, const string& txt)
{
    int M = pat.size();
    int N = txt.size();

    // 构造最长公共前后缀, 这是KMP算法最核心的部分
    vector<int> dp_table(M, 0);
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
    int j = 0;
    for(int i=0; i<txt.size(); i++)
    {
        if(txt[i] != pat[j])
            j = dp_table[j];
        else
        {   
            j++;
            if(j == pat.size())
                return i - pat.size() + 1;
        }
    }
    return -1;
}

int main()
{
    string pat = "ABABC";
    string txt = "CABAABABCC";
    int res = KMP(pat, txt);
    cout << res << endl;
    cout << txt.substr(res, pat.size()) << endl;
    return 0;
}