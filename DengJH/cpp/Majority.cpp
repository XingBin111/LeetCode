#include <iostream>
#include <vector>

using namespace std;

int majority_candidate(vector<int>& nums)
{
    int c = 0;
    int maj;
    for(int i=0; i<nums.size(); i++)
    {
        if(c == 0)
        {
            maj = nums[i];
            c = 1;
        }
        else
        {
            if(maj == nums[i])
                c++;
            else
                c--;
        }
    }
    return maj;
}

bool majority_check(vector<int>& nums, int maj)
{
    int occ = 0;
    for(auto& x: nums)
        if(x == maj)
            occ++;
    return 2 * occ > nums.size();
}

bool majority(vector<int>& nums)
{
    int maj = majority_candidate(nums);
    return majority_check(nums, maj);
}

int main()
{
    vector<int> nums = {1, 6, 8, 1, 9, 1, 2, 1, 1};
    vector<int> nums1 = {2, 1, 6, 1, 8, 1, 9, 1, 2, 1, 1};
    vector<int> nums2 = {1, 2, 3, 4, 5, 5, 6, 5, 1};
    cout << majority(nums) << endl;
    cout << majority(nums1) << endl;
    cout << majority(nums2) << endl;
    return 0;
}