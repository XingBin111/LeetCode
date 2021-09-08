#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

bool isPalindrome(const string& s)
{
    string::const_iterator begin_iter = s.begin();
    string::const_iterator end_iter = s.end();
    while (begin_iter < end_iter)
    {
        if(*begin_iter != *end_iter)
            return false;
        
        begin_iter++;
        end_iter--;
    }
    return true;
}

// 时间复杂度高达O(N^3), 差评
int longestPalindromeSubseq(const string& s)
{
    int n = s.size();
    vector<vector<int> > dp_table(n, vector<int>(n, 0));
    for(int i=0; i<n; i++)
        dp_table[i][i] = 1;
    
    for(int i=n-2; i>=0; i--)
    {
        for(int j=i+1; j<n; j++)
        {
            if(s[i] == s[j] && isPalindrome(s.substr(i, j-i+1))) 
                dp_table[i][j] = dp_table[i+1][j-1] + 2;
            else
                dp_table[i][j] = max(dp_table[i][j-1], dp_table[i+1][j]);
        }
    }
    return dp_table[0][n-1];
}

string extend(const string& s, int i, int j)
{   
    while(i>=0 && j<s.size() && s[i] == s[j])
    {
        i--;
        j++;
    }
    return s.substr(i+1, j-i-1);
}

// 时间效率为O(N^2)
string longestPalindromeSubseqExtend(const string& s)
{   
    string res = "";
    for(int i=0; i<s.size()-2; i++)
    {
        string s1 = extend(s, i, i);
        string s2 = extend(s, i, i+1);
        string max_len_s = s1.size() > s2.size() ? s1 : s2;
        res = max_len_s.size() > res.size() ? max_len_s : res;
    }
    return res;
}


string Manacher(string s) {
    // Insert '#'
    string t = "$#";
    for (int i = 0; i < s.size(); ++i) {
        t += s[i];
        t += "#";
    }
    
    int n = t.size();
    int* p = new int[n];
    int C = 0, R = 0;
    for(int i=1; i<n-1; i++)
    {
        int i_mirror = 2 * C - i;
        if(R > i)
            p[i] = min(R-i, p[i_mirror]);
        else
            p[i] = 0;
        
        // 不断向右拓展, 所有节点访问一次, 666
        while(t[i+1+p[i]] == t[i-1-p[i]])
            p[i]++;
        
        if(i+p[i]>R)
        {
            C = i;
            R = i + p[i];
        }
    }

    int max_len = 0;
    int center_idx = 0;
    for(int i=1; i<n-1; i++)
    {
        if(p[i] > max_len)
        {
            max_len = p[i];
            center_idx = i;
        }
    }
    int start = (center_idx - max_len) / 2;
    delete [] p;
    return s.substr(start, max_len);
}


int main()
{
    string s = "wabwsw";
    cout << Manacher(s) << endl;
    return 0;
}