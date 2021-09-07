#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <limits.h>

using namespace std;

class Solution{
    public:
        void rotate(vector<int>& nums, int k){
            int n = nums.size();
            k = k % n;
            int count = 0, start = 0;
            while(count < n){
                int cur_idx = start;
                int cur_val = nums[start];
                while (true)
                {
                    int nxt_idx = (cur_idx + k) % n;
                    swap(nums[nxt_idx], cur_val);
                    cur_idx = nxt_idx;
                    count++;
                    if(cur_idx == start)
                        break;
                }  
                start++;              
            }
            
        }
};

int main(){
    vector<int> nums = {1, 2, 3, 4, 5, 6, 7};
    int k = 3;
    Solution s;
    s.rotate(nums, k);

    for(int i=0; i<nums.size(); i++)
        cout << nums[i] << endl;
    return 0;
}