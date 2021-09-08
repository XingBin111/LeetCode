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
        if(needs.count(s[i]))
        {
            window[s[i]]++;
            if(window[s[i]] == needs[s[i]])
                match++;
        }

        if(i <=2)
            continue;

        if(needs.count(s[i-3]))
        {
            window[s[i-3]]--;
            if(window[s[i-3]] != needs[s[i-3]])
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