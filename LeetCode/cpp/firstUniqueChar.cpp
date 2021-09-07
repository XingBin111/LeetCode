/*

返回字符串中第一个非重复字符的下标, 如果不存在, 就返回-1.

*/

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <unordered_map>
#include <cmath>

using namespace std;

class Solution{
    public:
        int firstUniqueChar(string& s){
            unordered_map<char, int> map;
            int res = INT32_MAX;
            for(int i=0; i<s.size(); i++)
                if(map.count(s[i]))
                    map[s[i]] = INT32_MAX;
                else 
                    map[s[i]] = i;
            for(auto& x: map)
                res = min(res, x.second);
            return res == INT32_MAX ? -1 : res;
        }
};


int main(){
    string s1 = "loveleetcode";
    string s2 = "leetcode";
    string s3 = "aaabbbcc";
    Solution S;
    cout << S.firstUniqueChar(s1) << endl;
    cout << S.firstUniqueChar(s2) << endl;
    cout << S.firstUniqueChar(s3) << endl;
    return 0;
}