#include <iostream>
#include <vector>

using namespace std;

bool leftRightPointer(const vector<int>& nums, int target)
{
    vector<int>::const_iterator left = nums.begin();
    vector<int>::const_iterator right = nums.end() - 1;
    while(left != right)
    {
        if(*left + *right == target)
            return true;
        else if (*left + *right < target)
            left++;
        else
            right--;
    }
    return false;
}

int main()
{
    vector<int> nums = {2, 7, 11, 15};
    cout << leftRightPointer(nums, 9) << endl;
    cout << leftRightPointer(nums, 10) << endl;
    return 0;
}