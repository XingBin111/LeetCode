#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<int> partitionLabels(string S) {
        vector<int> res;
        int n = S.size();
        unordered_map<char, int> map;
        for(int i=0; i< n; i++)
            map[S[i]] = i;
        
        int i = 0;
        int j = 0;
        while(i < n){
            char c = S[i];
            j = map[c];
            if(j > i)
                for(int k=i+1; k<j; k++)
                    j = max(map[S[k]], j);
            res.push_back(j-i+1);
            i = j + 1;
        }
        return res;   
    }
};

int main(){
    string s = "ababcbacadefegdehijhklij";
    Solution S;
    vector<int> res = S.partitionLabels(s);
    for(auto &x: res)
        cout << x << endl;
    return 0;

}