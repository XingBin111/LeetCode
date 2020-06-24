#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include "limits.h"
#include <math.h>

using namespace std;

int trap(const vector<int>& nums)
{
    int n = nums.size();
    vector<int> l_max = vector<int>(n, nums[0]);
    vector<int> r_max = vector<int>(n, nums[n-1]);

    for(int i=n-2; i>=0; i--)
        r_max[i] = max(r_max[i+1], nums[i]);

    for(int i=1; i<n; i++)
        l_max[i] = max(l_max[i-1], nums[i-1]);

    int res = 0;
    for(int i=0; i<n; i++)
        res += max(min(l_max[i], r_max[i]) - nums[i], 0);
    return res;
}

int trapI(const vector<int>& nums)
{
    int n = nums.size();
    int left = 0;
    int right = n - 1;
    int l_max = nums[0];
    int r_max = nums[right];
    int res = 0;
    while(left <= right)
    {
        if(l_max < r_max)
        {
            res += max(l_max - nums[left], 0);
            l_max = max(nums[left], l_max);
            left++;
        }
        else
        {
            res += max(r_max - nums[right], 0);
            r_max = max(nums[right], r_max);
            right--;
        }   
    }
    return res;
}

int main()
{
    vector<int> nums = {0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1};
    cout << trap(nums) << endl;
    cout << trapI(nums) << endl;
    return 0;
}