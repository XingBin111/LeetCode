#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

string sliding_window(const string& s, const string& t)
{
    // 相当于两个计数器
    unordered_map<char, int> window;
    unordered_map<char, int> needs;
    for (char c : t) needs[c]++;

    int right = 0, left = 0;
    int start = 0, minLen = INT32_MAX;
    int match = 0;
    while (right < s.size())
    {
        char c1 = s[right];
        if(needs.count(c1))     // 如果c1在needs中存在, 就更新window和match
        {
            window[c1]++;
            if(window[c1] == needs[c1])
                match++;
        }

        while(match == needs.size())    // 开始优化
        {   
            if(minLen > (right - left + 1))
            {
                start = left;
                minLen = right - left + 1;
            }
            char c2 = s[left];
            if(needs.count(c2))
            {
                window[c2]--;
                if(window[c2] < needs[c2])
                    match--;
            }
            left++;
        }
        right++;
    }
    if(minLen==INT32_MAX)
        return "";
    return s.substr(start, minLen); 
}

int main()
{
    string s = "EBBANCF";
    string t = "ABC";
    cout << sliding_window(s, t) << endl;
    return 1;
}