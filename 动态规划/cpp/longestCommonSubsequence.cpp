#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <unordered_map>

using namespace std;

int longestCommonSubsequence(const string& s1, const string& s2)
{
    int M = s1.size();
    int N = s2.size();
    vector<vector<int> > dp_table(M+1, vector<int>(N+1, 0));
    for(int i=1; i<=M; i++)
    {
        for(int j=1; j<=N; j++)
        {
            if(s1[i-1] == s2[j-1])
                dp_table[i][j] = dp_table[i-1][j-1] + 1;
            else
                dp_table[i][j] = max({dp_table[i-1][j], dp_table[i][j-1]});            
        }
    }
    return dp_table[M][N];
}

int main()
{
    string s1 = "abcde";
    string s2 = "ace";
    cout << longestCommonSubsequence(s1, s2) << endl;
    return 0;
}