#include <iostream>
#include <vector>

using namespace std;

void swap(vector<int>& nums, int i, int j)
{
    int tmp = nums[j];
    nums[j] = nums[i];
    nums[i] = tmp;
}

// [hi, lo]
int partitionI(vector<int>& nums, int lo, int hi)
{
    int privot = nums[lo];
    while(lo < hi)
    {
        while(lo < hi && privot <= nums[hi])
            hi--;
        nums[lo] = nums[hi];

        while(lo < hi && privot >= nums[lo])
            lo++;
        nums[hi] = nums[lo];
    }
    nums[lo] = privot;
    return lo;
}

// L = [lo, mi], G = [mi+1, k-1], U = [k, hi]
int partitionII(vector<int>& nums, int lo, int hi)
{
    int privot = nums[lo];
    int mi = lo;
    for(int k=lo+1; k<=hi; k++)
    {
        if(nums[k] < privot)
        {
            swap(nums, mi+1, k);
            mi++;
        }
    }
    swap(nums, lo, mi);
    return mi;
}

// [lo, hi)
void quick_sort(vector<int>& nums, int lo, int hi)
{
    if(hi - lo < 2)
        return;
    int mi = partitionII(nums, lo, hi);
    quick_sort(nums, lo, mi);
    quick_sort(nums, mi+1, hi);
}

int main()
{
    vector<int> nums = {6, 3, 8, 2, 5, 9, 4, 5, 1, 7};
    quick_sort(nums, 0, nums.size());

    for(auto& x: nums)
        cout << x << endl;
    return 0;
}