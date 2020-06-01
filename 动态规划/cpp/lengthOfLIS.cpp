#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include "limits.h"

using namespace std;

// 时间效率为O(n^2)
int lengthOfLIS(const vector<int>& nums)
{
    vector<int> dp_table(nums.size(), 1);
    for(int i=1; i<dp_table.size(); i++)
    {   
        int tmp;
        for(int j=0; j<i; j++)
        {
            if(nums[i] > nums[j])
                tmp = dp_table[j] + 1;
            else
                tmp = dp_table[j];
            
            if(tmp > dp_table[i])
                dp_table[i] = tmp;
        }
    }  
    return dp_table[dp_table.size()-1];
}

// 时间效率为O(n*log(n))
int lengthOfLIS_binSearch(const vector<int>& nums)
{
    vector<int> dp_table(1, nums[0]);
    int piles = 1;
    for(int i=1; i<nums.size(); i++)
    {   
        int left = 0, right = piles - 1;
        while(left <= right)
        {
            int mid = left + (right - left) / 2;
            if(dp_table[mid] == nums[i])
                left = mid + 1;
            else if (dp_table[mid] > nums[i])
                right = mid - 1;
            else
                left = mid + 1;
        }
        if(left == piles)
        {
            piles++;
            dp_table.push_back(nums[i]);
        }
        else
        {
            dp_table[left] = nums[i];
        }
    }  
    return piles;
}

int main()
{
    vector<int> nums = {10, 9, 2, 5, 3, 7, 101, 18};
    int lis_length = lengthOfLIS_binSearch(nums);
    cout << lis_length << endl;
    return 0;
}