#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <unordered_map>

using namespace std;

int maxProfit(const vector<int>& nums)
{
    int n = nums.size();
    vector<vector<int> > dp_table(n, vector<int>(n, 0));

    for(int i=0; i<n; i++)
        dp_table[i][i] = nums[i];

    for(int i=n-2; i>=0; i--)
    {
        for(int j=i+1; j<n; j++)
        {
            dp_table[i][j] = max({nums[i] - dp_table[i+1][j], nums[j]-dp_table[i][j-1]});
        }
    }
    return dp_table[0][n-1];
}

int main()
{
    vector<int> nums = {3, 9, 1, 2};
    cout << maxProfit(nums) << endl;
    return 0;
}