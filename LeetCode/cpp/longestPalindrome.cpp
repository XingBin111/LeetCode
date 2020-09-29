/*
给定一个字符串求最长的回文子串, 如果存在多个的话就返回任意一个即可;

输入babad, 返回bab或aba

方法I: 使用动态规划, dp_table[i][j]==1表示s[i]~s[j]为回文子串, 那么迭代关系为:
dp_table[i][j] = dp_table[i+1][j-1] && (s[i] == s[j])

base case为:
dp_table[i][i] = 1
dp_table[i][i+1] = s[i] == s[i+1]

*/


#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

string longestPalindromeI(string& s){
    int n = s.size();
    if(n <= 1)
        return s;

    vector<vector<bool> > dp_table(n, vector<bool>(n, 1));
    string res = s.substr(0, 1);

    for(int i=0; i<n-1; i++)
        if(s[i] == s[i+1])
            res = s.substr(i, 2);
        else
            dp_table[i][i+1] = 0;
    
    for(int k=2; k<n; k++){
        for(int i=0; i<n-k; i++){
            int j = i + k;
            dp_table[i][j] = dp_table[i+1][j-1] && (s[i] == s[j]);
            if(dp_table[i][j] && (j - i + 1 > res.size()))
                res = s.substr(i, j-i+1);
        }
    }
    return res;
}

string longestPalindromeII(string s) {
        if (s.size() < 2)
            return s;
        int len = s.size(), max_left = 0, max_len = 1, left, right;
        for (int start = 0; start < len && len - start > max_len / 2;) {
            left = right = start;
            while (right < len - 1 && s[right + 1] == s[right])
                ++right;
            start = right + 1;
            while (right < len - 1 && left > 0 && s[right + 1] == s[left - 1]) {
                ++right;
                --left;
            }
            if (max_len < right - left + 1) {
                max_left = left;
                max_len = right - left + 1;
            }
        }
        return s.substr(max_left, max_len);
}


int main(){
    string s = "babad";

    string res = longestPalindromeII(s);
    cout << -12 % 10 << endl;
    cout << res << endl;
    return 0;
}