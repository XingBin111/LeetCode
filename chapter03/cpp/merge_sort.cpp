#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <stdlib.h>

using namespace std;

void merge(vector<int>& nums, int lo, int mid, int hi)
{
    vector<int> tmp_nums(nums.begin(), nums.end());
    
    int i = lo, j = mid + 1;
    for(int k=lo; k<hi+1; k++)
    {   
        int e = tmp_nums[k];
        if(i > mid)
        {
            nums[k] = tmp_nums[j];
            j++;
        }
        else if(j > hi)
        {
            nums[k] = tmp_nums[i];
            i++;
        }
        else if(tmp_nums[i] > tmp_nums[j])
        {
            nums[k] = tmp_nums[j];
            j++;
        }
        else
        {
            nums[k] = tmp_nums[i];
            i++;
        }
    }
}


void merge_sort(vector<int>& nums, int lo, int hi)
{
    if(lo == hi)
        return;
    
    int mid = (lo + hi) / 2;
   
    merge_sort(nums, lo, mid);  
    merge_sort(nums, mid+1, hi);
    merge(nums, lo, mid, hi);
}

int main()
{
    vector<int> nums = {3, 6, 1, 9, 7, 2, 4};
    merge_sort(nums, 0, nums.size()-1);
    for(auto& x: nums)
        cout << x << endl;
    return 0;
}