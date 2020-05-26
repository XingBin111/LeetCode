#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

vector<int> findAnagrams(const string& s, const string& t)
{
    unordered_map<char, int> window;
    unordered_map<char, int> needs;
    for (char c : t) needs[c]++;

    int right = 0, left = 0;
    int start = 0, minLen = INT32_MAX;
    int match = 0;
    vector<int> v;
    while(right < s.size())
    {
        char c1 = s[right];
        if(needs.count(c1))
        {
            window[c1]++;
            if(window[c1] == needs[c1])
                match++;
        }

        while(match == needs.size())
        {   
            v.push_back(left);
            char c2 = s[left];
            window[c2]--;
            if(window[c2] != needs[c2])
                match--;
            left++;
        }
        right++;
    }
    return v;
}

int main()
{
    string s = "cbaebabacd";
    string t = "abc";
    vector<int> v = findAnagrams(s, t);
    for(auto& x: v)
    {
        cout << s.substr(x, t.size()) << endl;
    }
}