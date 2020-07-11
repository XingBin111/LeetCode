#include <iostream>
#include <vector>
#include <stack>
#include <queue>

using namespace std;

class Solution {
public:
    void backtrack(vector<string>& v, int n, int left, int right, string s)
    {
        if(s.size() == 2*n)
        {
            v.push_back(s);
            return;
        }
        
        if(left < n)
            backtrack(v, n, left+1, right, s+'(');
        
        if(right < left)
            backtrack(v, n, left, right+1, s+')');
    }
    
    vector<string> generateParenthesis(int n) {
        vector<string> v;
        string s;
        backtrack(v, n, 0, 0, s);
        return v;
    }
};


int main()
{
    int n = 4;
    Solution s;
    vector<string> v = s.generateParenthesis(n);
    for(auto&x: v)
        cout << x << endl;
    return 0;
}