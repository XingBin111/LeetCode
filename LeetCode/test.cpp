#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums)
    {   
        int n = nums.size();
        for(int i=0; i<n; i++)
        {
            int tmp = abs(nums[i]);
            nums[tmp-1] = -abs(nums[tmp-1]);
        }
        vector<int> res;
        for(int i=0; i<n; i++)
        {
            if(nums[i]>0)
            {
                res.push_back(i+1);
            }
        }
        return res;
    }
};

int main()
{
    vector<int> arr = {4,3,2,7,8,2,3,1};
    Solution s;
    vector<int> k = s.findDisappearedNumbers(arr);
    //cout << k << endl;

    for(int i=0; i < k.size(); i++)
        cout << k[i] << endl;
    return 0;
}