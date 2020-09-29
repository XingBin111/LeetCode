#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <unordered_map>

using namespace std;

struct double_string
{
    string text;
    string pat;
    double_string(string _text="", string _pat="") : text(_text), pat(_pat) {}
    bool operator==(const double_string& ds) const {return (text==ds.text && pat==ds.pat);}
    friend ostream& operator<<(ostream& os, const double_string& ds)
    {
        os << "text: " << ds.text << ", pat: " << ds.pat << endl;
        return os;
    }
};

namespace std
{
    template<>
    struct hash<double_string>
    {
        size_t operator() (const double_string& s) const noexcept
        {
            return  hash<decltype(s.text)>()(s.text) +
                    hash<decltype(s.pat)>()(s.pat);
        }
    }; // 间接调用原生Hash.
}



bool isMatch(const string& text, const string& pat)
{   
    int M = text.size();
    int N = pat.size();

    if(N==0)
        return M==0;

    bool first_match = !text.empty() && (text[0] == pat[0] || pat[0] == '.');

    // *匹配0次或匹配1次
    if(N >= 2 && pat[1] == '*')
        return isMatch(text, pat.substr(2, N-2)) || (first_match && isMatch(text.substr(1, M-1), pat.substr(0, N)));
    else
        return first_match && isMatch(text.substr(1, M-1), pat.substr(1, N-1));
}

// 用字典又麻烦又慢
bool isMatchMemo(const string& text, const string& pat, unordered_map<double_string, bool>& memo)
{   
    
    int M = text.size();
    int N = pat.size();

    if(N==0)
        return M==0;
    
    double_string tmp(text, pat);
    if(memo.count(tmp))
        return memo[tmp];

    bool first_match = !text.empty() && (text[0] == pat[0] || pat[0] == '.');
    bool res;
    // *匹配0次或匹配1次
    if(N >= 2 && pat[1]== '*')
        res = isMatch(text, pat.substr(2, N-2)) || (first_match && isMatch(text.substr(1, M-1), pat));
    else
        res = first_match && isMatch(text.substr(1, M-1), pat.substr(1, N-1));
    memo[tmp] = res;
    return res;
}

// 用二维数组做memo
bool isMatchDP(string s, string p) {
        /**
         * f[i][j]: if s[0..i-1] matches p[0..j-1]
         * if p[j - 1] != '*'
         *      f[i][j] = f[i - 1][j - 1] && s[i - 1] == p[j - 1]
         * if p[j - 1] == '*', denote p[j - 2] with x
         *      f[i][j] is true iff any of the following is true
         *      1) "x*" repeats 0 time and matches empty: f[i][j - 2]
         *      2) "x*" repeats >= 1 times and matches "x*x": s[i - 1] == x && f[i - 1][j]
         * '.' matches any single character
         */
        int m = s.size(), n = p.size();
        vector<vector<bool>> f(m + 1, vector<bool>(n + 1, false));
        
        f[0][0] = true;
        for (int i = 1; i <= m; i++)
            f[i][0] = false;
        // p[0.., j - 3, j - 2, j - 1] matches empty iff p[j - 1] is '*' and p[0..j - 3] matches empty
        for (int j = 1; j <= n; j++)
            f[0][j] = j > 1 && '*' == p[j - 1] && f[0][j - 2];
        
        for (int i = 1; i <= m; i++)
            for (int j = 1; j <= n; j++)
                if (p[j - 1] != '*')
                    f[i][j] = f[i - 1][j - 1] && (s[i - 1] == p[j - 1] || '.' == p[j - 1]);
                else
                    // p[0] cannot be '*' so no need to check "j > 1" here
                    f[i][j] = f[i][j - 2] || (s[i - 1] == p[j - 2] || '.' == p[j - 2]) && f[i - 1][j];
        
        return f[m][n];

int main()
{
    string text = "aa";
    string pat = "a*";
    unordered_map<double_string, bool> memo;
    cout << isMatch(text, pat) << endl;
    return 0;
}
