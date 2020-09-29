/*
给定k和n找到1~9内不重复的k个数, 相加等于n

输入: k = 3, n = 7, 返回[[1,2,4]]
输入: k = 3, n = 9, 返回[[1,2,6], [1,3,5], [2,3,4]]
*/

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
private:
    vector<vector<int>> res;

public:
    void backtrack(int n, vector<int> combo, int new_start, int k){
        if(n == 0 && combo.size() == k){
            res.push_back(combo);
            return;
        }

        else if(n < 0 || combo.size() >= k)
            return;

        for(int i=new_start; i<=9; i++){
            combo.push_back(i);
            backtrack(n-i, combo, i+1, k);
            combo.pop_back();
        }
    }

    vector<vector<int>> combinationSum3(int k, int n) {
        vector<int> combo;
        backtrack(n, combo, 1, k);
        return res;
    }
};

int main(){
    int k = 3;
    int n = 9;
    Solution s;

    vector<vector<int>> res = s.combinationSum3(k, n);
    for(auto& x: res){
        for(auto& y: x)
            cout << y << "   ";
        cout << endl;
    }
        
            
    return 0;
}