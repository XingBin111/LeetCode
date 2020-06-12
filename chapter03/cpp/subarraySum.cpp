#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <stdlib.h>
#include <unordered_map>

using namespace std;

int subarraySumDict(const vector<int>& nums, int target)
{
    unordered_map<int, int> m;
    int ans = 0;
    m[0] = 1;

    int sum_i = 0, sum_j;
    for(int i=0; i<nums.size(); i++)
    {
        sum_i += nums[i];
        sum_j = sum_i - target;
        m[sum_i] = m[sum_i] + 1;
        if(m.count(sum_j))
            ans += m[sum_j];
    }
    return ans;
}

int main()
{
    vector<int> nums = {3, 5, 2, -2, 4, 1};
    int target = 8;
    cout << subarraySumDict(nums, target) << endl;
    return 0;
}