#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include "limits.h"
#include <math.h>

using namespace std;

int removeDuplicates(vector<int>& nums)
{
    int slow = 0;
    int fast = 1;
    int n = nums.size();
    while(fast < n)
    {
        if(nums[slow] != nums[fast])
            nums[++slow] = nums[fast];
        fast++;
    }
    return slow+1;
}

int main()
{
    vector<int> nums = {0, 0, 1, 1, 2, 2, 3, 3, 4};
    int res = removeDuplicates(nums);
    cout << res << endl;

    for(int i=0; i<nums.size(); i++)
        cout << nums[i] << endl;
    return 0;
}