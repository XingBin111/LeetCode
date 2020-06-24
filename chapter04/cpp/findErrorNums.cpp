#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include "limits.h"
#include <math.h>

using namespace std;

vector<int> findErrorNums(vector<int> nums)
{
    int dup = 0;
    int mis = 0;
    int n = nums.size();
    for(int i=0; i<n; i++)
    {
        int idx = abs(nums[i]);
        if(nums[idx] < 0)
            dup = abs(nums[i]);
        else
            nums[idx] *= -1;
    }

    for(int i=0; i<n; i++)
    {
        if(nums[i] > 0)
        {
            mis = i;
            break;
        }
    }
    return vector<int>({dup, mis});
}

int main()
{   
    int a[] = {0, 4, 1, 4, 2};
    vector<int> nums(5, 0);
    for(int i=0; i<5; i++)
        nums[i] = a[i];

    vector<int> res = findErrorNums(nums);
    cout << res[0] << endl;
    cout << res[1] << endl;
    return 0;
}