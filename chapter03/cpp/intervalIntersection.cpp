#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <stdlib.h>

using namespace std;

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

vector<vector<int> > interval_intersection(vector<vector<int> >& nums1, vector<vector<int> >& nums2)
{
    int m = nums1.size();
    int n = nums2.size();

    int i = 0, j = 0;
    vector<vector<int> > res;
    while(i < m && j < n)
    {   
        int a1 = nums1[i][0];
        int a2 = nums1[i][1];

        int b1 = nums2[j][0];
        int b2 = nums2[j][1];
        if(a2 >= b1 && b2 >= a1)
            res.push_back({max({a1, b1}), min({a2, b2})});

        if(a1 > b1)
            j++;
        else
            i++;
    }
    return res;
}


int main()
{
    vector<vector<int> > nums1 = {{0, 2}, {5, 10}, {13, 23}, {24, 25}};
    vector<vector<int> > nums2 = {{1, 5}, {8, 12}, {15, 24}, {25, 26}};
    vector<vector<int> > res = interval_intersection(nums1, nums2);
    show(res);
    return 0;
}