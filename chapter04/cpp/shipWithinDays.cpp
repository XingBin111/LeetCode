#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include "limits.h"
#include <math.h>

using namespace std;

int ship_time(const vector<int>& nums, int v)
{
    int res = 0;
    int s = 0;
    for(int i=0; i< nums.size(); i++)
    {
        s += nums[i];
        if(s > v)
        {
            s = nums[i];
            res ++;
        }
    }
    if(s > 0)
        res++;
    return res;
}

int shipWithinDays(const vector<int>& nums, int d)
{
    int lo = nums[0];
    int hi = nums[0];
    int n = nums.size();
    for(int i=1; i<n; i++)
    {
        if(lo < nums[i])
            lo = nums[i];
        hi += nums[i];
    }

    while(lo <= hi)
    {
        int mid = (hi + lo) / 2;
        int t = ship_time(nums, mid);
        if(t > d)
            lo = mid + 1;       // 速度增加
        else    
            hi = mid - 1;       // 速度降低
    }
    return lo;
}

int main()
{
    vector<int> nums = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int d = 5;
    cout << shipWithinDays(nums, d) << endl;
    return 0;
}