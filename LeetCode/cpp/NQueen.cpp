#include <iostream>
#include <vector>
#include <stack>
#include <queue>

using namespace std;

class Solution {
public:
    
    struct queen
    {
        int i;
        int j;
        queen(int _i, int _j) : i(_i), j(_j) {};
        bool is_conflict(int x, int y) 
        {
            if(i == x || j == y || x-y == i-j || x+y == i+j)
                return true;
            else
                return false;
        };
    };
    
    void isConflict(vector<int>& nums, vector<int>& track, int& res)
    {
        if(nums.size() == track.size())
        {
            res++;
            cout << res << endl;
            return;
        }
        
        for(int i=0; i<nums.size(); i++)
        {   
            int n = track.size();
            int e = nums[i];
            bool flag = false;
            for(int j=0; j<n; j++)
            {
                queen t(j, track[j]);
                if(t.is_conflict(n, e))
                {
                    flag = true;
                    break;
                }
            }   
            if(flag)
                continue;
            
            track.push_back(e);
            isConflict(nums, track, res);
            track.pop_back();
        }
    }   
    
    int totalNQueens(int n) {
        vector<int> nums(n, 0);
        vector<int> track;
        int res = 0;
        for(int i=0; i<n; i++)
            nums[i] = i;
        
        isConflict(nums, track, res);
        return res;
    }
};

int main()
{
    Solution s;
    cout << s.totalNQueens(4) << endl;
    return 0;
}