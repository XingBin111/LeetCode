#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <stdlib.h>

using namespace std;

 
bool myfunction (const vector<int>& i,const vector<int>& j) { return (i[0]<j[0]); }

vector<vector<int> > interval_merge(vector<vector<int> >& nums)
{
    sort(nums.begin(), nums.end(), myfunction);
    vector<vector<int> > res = {nums[0]};

    for(int i=1; i<nums.size(); i++)
    {   
        // merge
        if(nums[i][0] < nums[i-1][1])
            res[res.size()-1][1] = nums[i][1];
        else
            res.push_back(nums[i]);
    }
    return res;
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

int main()
{
    vector<vector<int> > nums = {{1, 3}, {2, 6}, {8, 10}, {15, 18}};
    vector<vector<int> > res = interval_merge(nums);
    show(res);
    return 0;
}