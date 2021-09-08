#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include "limits.h"

using namespace std;

int lengthOfLongestSubstring(string s)
{
    unordered_map<char, int> window;
    
    int left = 0, right = 0;
    int match = 0, max_len = INT_MIN;
    while(right < s.size())
    {
        char c1 = s[right];
        window[c1]++;
        while(window[c1] > 1)
        {
            char c2 = s[left];
            window[c2]--;
            left++;
        }
        
        if(max_len < (right - left + 1))
            max_len = right - left + 1;

        right++;
    }
    return max_len;
}

int main()
{
    string s = "abcabcdb";
    cout << lengthOfLongestSubstring(s) << endl;
}