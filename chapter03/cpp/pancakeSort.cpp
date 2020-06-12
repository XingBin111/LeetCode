#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <stdlib.h>
#include <stack>

using namespace std;

int find_max_idx(vector<int>& nums, int k)
{
    int max_idx = 0;
    int max_val = nums[0];
    for(int i=1; i<k+1; i++)
    {
        if(nums[i] > max_val)
        {
            max_idx = i;
            max_val = nums[i];
        }
    }
    return max_idx;
}

void reverse_vector(vector<int>& nums, int k)
{
    int i = 0;
    int j = k;
    while(i < j)
    {
        swap(nums[i], nums[j]);
        i++;
        j--;
    }
}

vector<int> pancakeSort(vector<int>& nums)
{   
    vector<int> opt;
    int n = nums.size();
    for(int i=n-1; i>0; i--)
    {
        int max_idx = find_max_idx(nums, i);
        if(max_idx != i)
        {   
            if(max_idx != 0)
            {
                reverse_vector(nums, max_idx);
                opt.push_back(max_idx + 1);
            }
            reverse_vector(nums, i);
            opt.push_back(i+1);
        }
    }
    return opt;
}


int main()
{
    vector<int> nums = {3, 2, 4, 1};
    vector<int> opt = pancakeSort(nums);
    if(opt.size() > 0)
    {
        for(auto& x: opt)
        cout << x << endl;
    }
    else
        cout << "Empty opt!\n";
    
    return 0;
}