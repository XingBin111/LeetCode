#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <unordered_map>

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
                dp_table[i][j] = max({dp_table[i][j-1], dp_table[i+1][j]});
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

int main()
{
    string s = "awkca";
    cout << longestPalindromeSubseqExtend(s) << endl;
    return 0;
}