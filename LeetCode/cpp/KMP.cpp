#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution{
    public:
        vector<int> build_next(string& pat){
            vector<int> dp(pat.size(), -1);
            int t = -1, j = 0;
            while(j < pat.size() - 1){
                if(t < 0 || pat[t] == pat[j]){
                    t++; j++;
                    dp[j] = pat[t] == pat[j] ? dp[t] : t;
                }
                else
                    t = dp[t];
            }
            return dp;
        }

        int kmp(string txt, string pat){
            int m = txt.size(), n = pat.size();
            vector<int> dp = build_next(pat);
            int i = 0, j = 0;
            while(i < m && j < n){
                
                if(j < 0 || pat[j] == txt[i]){
                    i++; j++;
                }
                else
                    j = dp[j];
                if(j == n)
                    return i - j;
            }
            return -1;
        }
};


int main(){
    Solution S;
    string txt = "hello";
    string pat = "ll";
    cout << S.kmp(txt, pat) << endl;
    return 0;
}