/* 
给定4个0~9的整数, 返回能组成最大的时间,(最大的时间为23:59, 最小时间为00:00)
例1: [1, 2, 3, 4], 返回"23:41"
例2: [5, 5, 5, 5], 返回"""

使用回溯算法找到所有可能的组合, 从组合里面选最大的时间. 普通的回溯无法处理重复元素的情况[0, 0, 0, 0], 所以这里的track是下标的集合.
*/

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    
    bool valid(const vector<int>& track){
        if(track[0] == 2 && track[1] <= 3 && track[2] <= 5 && track[3] <= 9)
            return true;
        if(track[0] <= 1 && track[1] <= 9 && track[2] <= 5 && track[3] <= 9)
            return true;
        else
            return false;
    }
    
    int cal(const vector<int>& track)
    {
        int tmp = track[0] * 1000 + track[1] * 100 + track[2] * 10 + track[3];
        return tmp;
    }
    
    void backtrack(const vector<int>& A, vector<int>& track, vector<int>& res)
    {
        if(track.size() == A.size()){
            vector<int> tmp = {A[track[0]], A[track[1]], A[track[2]], A[track[3]]};
            if(valid(tmp) && cal(tmp) > cal(res))
                for(int i=0; i<res.size(); i++)
                    res[i] = tmp[i];
            return;
        }
        
        for(int i=0; i<A.size(); i++){
            if(find(track.begin(), track.end(), i) != track.end())
                continue;
            track.push_back(i);
            backtrack(A, track, res);
            track.pop_back();
        }
    }
    
    string largestTimeFromDigits(vector<int>& A) {
        vector<int> track;
        vector<int> res = {-1, -1, -1, -1};
        backtrack(A, track, res);
        for(auto& x: res)
            cout << x << endl;
        if(res[0] == -1)
            return "";
        else{
            string s = "";
            s += res[0] + '0';
            s += res[1] + '0';
            s += ':';
            s += res[2] + '0';
            s += res[3] + '0';
            return s;
        }
    }
};

int main(){
    vector<int> A = {0, 4, 0, 0};
    Solution S;

    string s = S.largestTimeFromDigits(A);
    cout << s << endl;
    return 0;
}