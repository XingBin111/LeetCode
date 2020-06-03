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
    bool first_match = (text[0] == pat[0] || pat[0] == '.');

    // *匹配0次或匹配1次
    if(N >= 2 && pat[1]== '*')
        return isMatch(text, pat.substr(2, N-2)) || (first_match && isMatch(text.substr(1, M-1), pat.substr(0, N)));
    else
        return first_match && isMatch(text.substr(1, M-1), pat.substr(1, N-1));
}

bool isMatchMemo(const string& text, const string& pat, unordered_map<double_string, bool>& memo)
{   
    int M = text.size();
    int N = pat.size();

    if(N==0)
        return M==0;
    
    double_string tmp(text, pat);
    if(memo.count(tmp))
        return memo[tmp];

    bool first_match = (text[0] == pat[0] || pat[0] == '.');
    bool res;
    // *匹配0次或匹配1次
    if(N >= 2 && pat[1]== '*')
        res = isMatch(text, pat.substr(2, N-2)) || (first_match && isMatch(text.substr(1, M-1), pat.substr(0, N)));
    else
        res = first_match && isMatch(text.substr(1, M-1), pat.substr(1, N-1));
    memo[tmp] = res;
    return res;
}

int main()
{
    string text = "aaa";
    string pat = "a*";
    unordered_map<double_string, bool> memo;
    cout << isMatchMemo(text, pat, memo) << endl;
    return 0;
}
