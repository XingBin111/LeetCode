#include <iostream>
#include <vector>

using namespace std;

int binSearch(const vector<int>& nums, int target)
{
    int left = 0;
    int right = nums.size() - 1;
    while(left <= right)
    {
        int mid = left + (right - left) / 2;
        if(nums[mid] == target)
            return mid;
        else if (nums[mid] < target)
        {
            left = mid + 1;
        }
        else if (nums[mid] > target)
        {
            right = mid - 1;
        }
    }
    return -1;
}

int binSearchLeftBound(const vector<int>& nums, int target)
{
    int left = 0;
    int right = nums.size();
    while(left <= right)
    {
        int mid = left + (right - left) / 2;
        if(nums[mid] == target)
            right = mid - 1;
        else if (nums[mid] < target)
        {
            left = mid + 1;
        }
        else if (nums[mid] > target)
        {
            right = mid - 1;
        }
    }
    if(left==nums.size() || nums[left] != target)
        return -1;
    return left;
}

int binSearchRightBound(const vector<int>& nums, int target)
{
    int left = 0;
    int right = nums.size();
    while(left <= right)
    {
        int mid = left + (right - left) / 2;
        if(nums[mid] == target)
            left = mid + 1;
        else if (nums[mid] < target)
        {
            left = mid + 1;
        }
        else if (nums[mid] > target)
        {
            right = mid - 1;
        }
    }
    if(right==-1 || nums[right] != target)
        return -1;
    return right;
}

void usage(const vector<int>& nums, const vector<int>& target, int (pfunc)(const vector<int>&, int))
{   
    cout << "nums: ";
    for(int i=0; i<nums.size(); i++)
        cout << nums[i] << ", ";
    cout << endl;
    cout << "find target in nums: \n";
    for(int i=0; i<target.size(); i++)
    {   
        cout << "target: " << target[i] << ", index:" << pfunc(nums, target[i]) << endl;
    }
}

int main()
{
    vector<int> nums = {1, 2, 2, 2, 3, 4, 6, 7, 8};
    vector<int> target = {0, 2, 4, 5, 9};
    
    cout << "------------usage of binSearch------------\n";
    usage(nums, target, binSearch);
    
    cout << endl;

    cout << "------------usage of binSearchLeftBound------------\n";
    usage(nums, target, binSearchLeftBound);

    cout << endl;

    cout << "------------usage of binSearchRightBound------------\n";
    usage(nums, target, binSearchRightBound);

    return 0;
}