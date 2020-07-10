#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <algorithm> 

using namespace std;

class Solution {
public:
    static bool cmp(vector<int> v1, vector<int> v2){
        return v1[0] < v2[0];
    }

    void from_left(const vector<vector<int>>& buildings, vector<vector<int>>& res)
    {   
        int h = buildings[0][2];
        int right = buildings[0][1];
        int left = buildings[0][0];
        res.push_back({left, h});
        for(int i=1; i<buildings.size(); i++)
        {   
            if(buildings[i][0] == left && buildings[i][1] == right)
            {
                res[res.size()-1][1] = max(buildings[i][2], res[res.size()-1][1]);
            }
            else if(buildings[i][0] > right)
            {
                res.push_back({buildings[i][0], buildings[i][2]});
            }

            else if(buildings[i][2] > h)
            {
                res.push_back({buildings[i][0], buildings[i][2]});
            }
            h = buildings[i][2];
            right = buildings[i][1];
            left = buildings[i][0]; 
        }
    }

    void from_right(const vector<vector<int>>& buildings, vector<vector<int>>& res)
    {   
        int n = buildings.size();
        int h = buildings[n-1][2];
        int right = buildings[n-1][1];
        int left = buildings[n-1][0];
        res.push_back({right, 0});
        for(int i=n-2; i>=0; i--)
        {   
            if(buildings[i][0] == left && buildings[i][1] == right)
            {
                res[res.size()-1][1] = max(buildings[i][2], res[res.size()-1][1]);
            }
            else if(buildings[i][1] < left)
            {
                res.push_back({buildings[i][1], 0});
            }

            else if(buildings[i][2] > h)
            {
                res.push_back({buildings[i][1], h});
            }
            h = buildings[i][2];
            right = buildings[i][1];
            left = buildings[i][0]; 
        }
    }

    vector<vector<int>> getSkyline(vector<vector<int>>& buildings) {
        int n = buildings.size();
        vector<vector<int>> res;
        if(n == 0)
            return res;
        
        from_left(buildings, res);
        from_right(buildings, res);
        //sort(res.begin(), res.end(), cmp);
        return res;
    }
};


int main()
{
    // vector<vector<int> > nums = {{2, 9, 10}, {3, 7, 15}, {5, 12, 12}, {15, 20, 10}, {19, 24, 8}};
    vector<vector<int> > nums = {{2, 4, 7}, {2, 4, 5}, {2, 4, 6}};
    Solution s;
    vector<vector<int> > res = s.getSkyline(nums);
    for(auto&x: res)
    {
        for(auto& y: x)
            cout << y << "   ";
        cout << endl;
    }

    return 0;
}