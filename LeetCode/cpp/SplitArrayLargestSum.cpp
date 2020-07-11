#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <algorithm> 

using namespace std;

class Solution {
public:
    int splitArray(vector<int>& nums, int m) {
        int left = nums[0];
        long long int right = 0;
        int n = nums.size();
        for(int i=0; i<=n; i++)
        {
            right += nums[i];
            left = max(left, nums[i]);
        }
        
        while(left <= right)
        {
            long long int mid = left + (right - left) / 2;
            int count = 0;
            int s = 0;
            for(int i=0; i<n; i++)
            {
                if(s + nums[i] > mid)
                {
                    count++;
                    s = nums[i];
                }
                else
                    s += nums[i];
            }
            if(s > 0)
                count++;
            
            if(count <= m)
                right = mid - 1;
            else
                left = mid + 1;
        }
        return left;
    }
};

int main()
{
    vector<int> nums = {7,2,5,10,8};
    int m = 2;
    Solution s;
    cout << s.splitArray(nums, m) << endl;
    return 0;
}