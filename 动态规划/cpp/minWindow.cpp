#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include "limits.h"

using namespace std;

string minWindow(const string& s, const string& t)
{
    unordered_map<char, int> window;
    unordered_map<char, int> needs;
    for(char x: t)
        needs[x]++;
    int match = 0;
    int slow = 0, fast = 0;
    int start = 0, min_len = INT_MAX;

    while(fast < s.size())
    {   
        // 更新window和match
        char c1 = s[fast];
        if(needs.count(c1))
        {
            window[c1]++;
            if(window[c1] == needs[c1])
                match++;
        }
        
        // 优化
        while(match == needs.size())
        {   
            
            // 记录最小长度
            if(fast-slow + 1 < min_len)
            {
                
                min_len = fast - slow + 1;
                start = slow;
            }

            // slow右移一位, 并更新window和match
            char c2 = s[slow];
            if(needs.count(c2))
            {
                window[c2]--;
                if(window[c2] < needs[c2])
                    match--;
            }
            slow++;
        }

        fast++;
    }
    return min_len == INT_MAX ? "" : s.substr(start, min_len);
}

int main()
{
    string s = "EBBANCF";
    string t = "ABC";
    cout << minWindow(s, t) << endl;
    return 0;
}