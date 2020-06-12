#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <stdlib.h>

using namespace std;

bool is_in_area(const vector<vector<int> >& nums, int x, int y)
{
    int m = nums.size();
    int n = nums[0].size();

    if(x >= 0 && x < m && y >= 0 && y < n)
        return true;
    else
        return false;
}

// 该版本在old_color=new_color时会陷入死循环, 所以要记录搜索过的地方
void flood_fill(vector<vector<int> >& nums, int x, int y, int old_color, int new_color)
{   
    if(!is_in_area(nums, x, y))
        return;

    if(nums[x][y] != old_color)
        return;

    nums[x][y] = new_color;

    flood_fill(nums, x+1, y, old_color, new_color);
    flood_fill(nums, x-1, y, old_color, new_color);
    flood_fill(nums, x, y+1, old_color, new_color);
    flood_fill(nums, x, y-1, old_color, new_color);
}

int flood_fill_boundary(vector<vector<int> >& nums, int x, int y, int old_color, int new_color, vector<vector<bool> > &visited)
{   
    if(!is_in_area(nums, x, y))
        return 0;

    if(visited[x][y])
        return 1;

    if(nums[x][y] != old_color)
        return 0;
    
    visited[x][y] = true;
    int res = flood_fill_boundary(nums, x+1, y, old_color, new_color, visited) +
            flood_fill_boundary(nums, x-1, y, old_color, new_color, visited) +
            flood_fill_boundary(nums, x, y+1, old_color, new_color, visited) +
            flood_fill_boundary(nums, x, y-1, old_color, new_color, visited);
    if(res < 4)
        nums[x][y] = new_color;
    return 1;

}

// 使用visited来标记已经遍历过的像素.
void flood_fill_better(vector<vector<int> >& nums, int x, int y, int old_color, int new_color, vector<vector<bool> > &visited)
{   
    if(!is_in_area(nums, x, y))
        return;

    if(visited[x][y])
        return;
        
    if(nums[x][y] != old_color)
        return;

    visited[x][y] = true;
    flood_fill_better(nums, x+1, y, old_color, new_color, visited);
    flood_fill_better(nums, x-1, y, old_color, new_color, visited);
    flood_fill_better(nums, x, y+1, old_color, new_color, visited);
    flood_fill_better(nums, x, y-1, old_color, new_color, visited);

    nums[x][y] = new_color;
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
    vector<vector<int> > nums = {{1, 1, 1, 1}, {1, 1, 1, 0}, {1, 1, 0, 1}, {1, 0, 1, 1}};
    vector<vector<bool> > visited(nums.size(), vector<bool>(nums[0].size(), false));
    int x = 1, y = 1;
    int old_color = nums[x][y];
    int new_color = 2;
    cout << "before flood fill:\n";
    show(nums);
    flood_fill_better(nums, x, y, old_color, new_color, visited);    

    cout << endl;
    cout << "after flood fill:\n";
    show(nums);
    return 0;
}