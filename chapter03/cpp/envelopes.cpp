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
    vector<int> res(0, nums.size());
    for(int i=0; i<nums.size(); i++)
        res[i] = nums[i][1];

    return 0;
}

int main()
{
    vector<vector<int> > nums = {{5, 4}, {6, 4}, {6, 7}, {2, 3}};
    sort(nums.begin(), nums.end(), myfunction);
    show(nums);
    return 0;
}