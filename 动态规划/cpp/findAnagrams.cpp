#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include "limits.h"

using namespace std;

vector<int> findAnagrams(const string& s, const string& p)
{
    unordered_map<char, int> window;
    unordered_map<char, int> needs;
    for(char x: p)
        needs[x]++;
    int left = 0, right = 0;
    int match = 0;
    vector<int> res;
    for(int i=0; i<s.size(); i++)
    {
        if(match == p.size())
            res.push_back(i-3);
        char c1 = s[i];
        if(needs.count(c1))
        {
            window[c1]++;
            if(window[c1] == needs[c1])
                match++;
        }

        if(i <=2)
            continue;

        char c2 = s[i-3];
        if(needs.count(c2))
        {
            window[c2]--;
            if(window[c2] != needs[c2])
                match--;
        }
    }
    return res;
}

int main()
{
    string s = "cbaebabacdasdbczabdabcbac";
    string p = "abc";
    vector<int> v = findAnagrams(s, p);
    for(auto& x: v)
    {
        cout << s.substr(x, p.size()) << endl;
    }
    return 0;

}