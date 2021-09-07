#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <unordered_map>

using namespace std;

struct double_string{
    string s1;
    string s2;
    double_string(string _s1, string _s2) {s1 = _s1; s2 = _s2;}
    friend ostream& operator<<(ostream& os, const double_string ds){
        os << "string 1: " << ds.s1 << ", string 2: " << ds.s2 <<endl;
        return os;
    }
};

int minDistanceIteration(const string& s1, const string& s2){
    vector<vector<int>> dp(s1.size()+1, vector<int>(s2.size()+1, 0));
    for(int i=1; i<=s1.size(); i++)
        dp[i][0] = i;
    
    for(int i=1; i<=s2.size(); i++)
        dp[0][i] = i;
    
    for(int i=1; i<=s1.size(); i++){
        for(int j=i; j<=s2.size(); j++){
            if(s1[i-1] == s2[j-1])
                dp[i][j] = dp[i-1][j-1];
            
            else
                dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1;
        }
    }
    return dp[s1.size()][s2.size()];

}

