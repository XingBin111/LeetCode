#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include "limits.h"
#include <math.h>

using namespace std;

int eating_time(const vector<int>& nums, int s)
{
    int res = 0;
    double s_d = (double) s;
    for(const auto& x: nums)
    {
        // cout << ceil(x / s_d) << endl;
        res += ceil(x / s_d);
    }
    return res;
}


int min_eating_speed(const vector<int>& nums, int h)
{
    int max_element = nums[0];
    int min_element = nums[0];
    int n = nums.size();
    for(int i=1; i<n; i++)
    {
        if(nums[i] > max_element)   
            max_element = nums[i];
        if(nums[i] < min_element)
            min_element = nums[i];
    }
    
    int left = min_element;
    int right = max_element;
    while(left <= right)
    {
        int mid = (right + left) / 2;
        int t = eating_time(nums, mid);
        if(t > h)
            left = mid + 1;         // 速度增加
        else    
            right = mid - 1;        // 速度降低
    }
    return left;

}

int main()
{
    int h = 8;
    vector<int> nums = {3, 6, 7, 11};
    cout << min_eating_speed(nums, h) << endl;
    return 0;
}