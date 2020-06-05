#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <stdlib.h>
#include <stack>

using namespace std;

vector<int> next_greater_element(const vector<int>& nums)
{   
    int n = nums.size();
    vector<int> res(n, 0);
    stack<int> s;
    for(int i=n-1; i>=0; i--)
    {   
        while(s.size() > 0 && s.top() < nums[i])
            s.pop();
            
        res[i] = s.size() > 0 ? s.top() : -1;
        s.push(nums[i]);
    }
    return res;
}

vector<int> next_greater_element_circle(const vector<int>& nums)
{   
    int n = nums.size();
    vector<int> res(n, 0);
    stack<int> s;
    for(int i = 2 * n - 1; i >= 0; i--)
    {   
        while(s.size() > 0 && s.top() <= nums[i%n])
            s.pop();
            
        res[i%n] = s.size() > 0 ? s.top() : -1;
        s.push(nums[i%n]);
    }
    return res;
}

vector<int> next_greater_element_idx(const vector<int>& nums)
{   
    int n = nums.size();
    vector<int> res(n, 0);
    stack<int> s;
    for(int i = n - 1; i >= 0; i--)
    {   
        while(s.size() > 0 && nums[s.top()] <= nums[i])
            s.pop();
            
        res[i] = s.size() > 0 ? s.top() : -1;
        s.push(i);
    }
    return res;
}

int main()
{
    vector<int> nums = {2, 1, 2, 4, 3};
    vector<int> res = next_greater_element_idx(nums);
    for(auto& x: res)
        cout << x << endl;
    return 0;
}