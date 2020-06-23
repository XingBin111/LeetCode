#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include "limits.h"

using namespace std;

// 指针从后往前移动
int edit_distance(const string& s1, const string& s2)
{   
    int m = s1.size();
    int n = s2.size();
    if(m == 0)
        return n;
    if(n == 0)
        return m;
    if(s1[m-1] == s2[n-1])
        return edit_distance(s1.substr(0, m-1), s2.substr(0, n-1));
    else
    {
        int res = min(
            {
                edit_distance(s1.substr(0, m), s2.substr(0, n-1)),        // 插入
                edit_distance(s1.substr(0, m-1), s2.substr(0, n)),        // 删除
                edit_distance(s1.substr(0, m-1), s2.substr(0, n-1)),      // 替换
            }
        );
        return res + 1;
    }
}

int edit_distance_iteration(const string& s1, const string& s2)
{
    int m = s1.size();
    int n = s2.size();
    vector<vector<int> > nums(n+1, vector<int>(m+1, 0));
    for(int i=0; i<=n; i++)
        nums[i][0] = i;
    
    for(int i=0; i<=m; i++)
        nums[0][i] = i;

    for(int i=1; i<=n; i++)
    {
        for(int j=1; j<=m; j++)
        {
            if(s2[i-1] == s1[j-1])
                nums[i][j] = nums[i-1][j-1];
            else
            {
                int res = min(
                    {
                        nums[i-1][j],
                        nums[i][j-1],
                        nums[i-1][j-1]
                    }
                );
                nums[i][j] = res + 1;
            }
        }
    }
    return nums[n][m];
}

int main()
{
    string s1 = "horse";
    string s2 = "ros";
    cout << edit_distance(s1, s2) << endl;
    cout << edit_distance_iteration(s1, s2) << endl;
    return 0;
}