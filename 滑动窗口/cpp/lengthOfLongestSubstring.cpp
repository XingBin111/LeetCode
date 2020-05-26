#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>


using namespace std;

string lengthOfLongestSubstring(const string& s)
{
    unordered_map<char, int> window;

    int right = 0, left = 0;
    int start = 0, maxLen = 0;
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

        if(right - left + 1 > maxLen)
        {
            start = left;
            maxLen = right - left + 1;
        }
        right++;
    }
    return s.substr(start, maxLen);
}

int main()
{
    vector<string> v = {"abcabcbb", "bbbbb", "pwwkew"};
    for(auto& x: v)
        cout << lengthOfLongestSubstring(x) << endl;
    return 0;
}