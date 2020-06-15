#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <stdlib.h>

using namespace std;

bool myfunction(const vector<int>& i,const vector<int>& j) 
{ 
    if(i[0] < j[0])
        return true;
    else if(i[0] > j[0])
        return false;
    else
    {
        if(i[1] < j[1])
            return false;
        else
            return true;
    }
}

void show(const vector<vector<int> >& nums)
{
    int m = nums.size();
    int n = nums[0].size();
    for(int i=0; i<m; i++)
    {
        for(int j=0; j<n; j++)
        {
            cout << nums[i][j] << "   ";
        }
        cout << endl;
    }
}

int lis(const vector<int>& nums)
{
    return 0;
}

int envelopes(const vector<vector<int> >& nums)
{
    vector<int> height(nums.size(), 0);
    for(int i=0; i<nums.size(); i++)
        height[i] = nums[i][1];

    int piles = 1;
    vector<int> res(1, height[0]);
    for(int i=1; i<height.size(); i++)
    {   
        int right = res.size();
        int h = height[i];
        if(h > res[right-1])
        {
            res.push_back(h);
            piles++;
        }
        else
        {
            int left = 0;
            while(left < right)
            {
                int mid = (left + right) / 2;
                if(height[mid] >= h)
                    right = mid;
                else
                    left = mid + 1;
            }
            res[piles] = height[left];
        }
    }
    return piles;
}

int main()
{
    vector<vector<int> > nums = {{5, 4}, {6, 4}, {6, 7}, {2, 3}};
    sort(nums.begin(), nums.end(), myfunction);
    show(nums);
    cout << envelopes(nums) << endl;
    return 0;
}