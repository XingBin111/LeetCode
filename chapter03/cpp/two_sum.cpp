#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <stdlib.h>
#include <unordered_map>

using namespace std;

bool two_sum(const vector<int>& nums, const int target)
{   
    unordered_map<int, int> m;
    for(int i=0; i<nums.size(); i++)
        m[nums[i]] = i;
    
    for(int i=0; i<nums.size(); i++)
    {
        int k = target - nums[i];
        if(m.count(k) && m[k] != i)
            return true;
    }
    return false;
}

int main()
{
    vector<int> nums = {3, 1, 2, 4, 6};
    int target = 6;
    cout << two_sum(nums, target) << endl;
    return 0;
}