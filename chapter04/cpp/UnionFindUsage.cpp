#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include "limits.h"
#include <math.h>
#include <stdlib.h>

using namespace std;

class UnionFind
{
    private:
        int count;
        vector<int> parent;
        vector<int> size;
    public:
        UnionFind(int n)
        {
            parent = vector<int>(n, 1);
            for(int i=0; i<n; i++)
                parent[i] = i;
            size = vector<int>(n, 1);
            count = n;
        };

        int find(int x)
        {
            while(parent[x] != x)
                x = parent[x];
            return x;
        };

        void union_pq(int p, int q)
        {   
            int root_p = find(p);
            int root_q = find(q);
            if(root_q != root_p)
            {   
                if(size[root_p] > size[root_q])
                {
                    parent[root_q] = parent[root_p];
                    size[root_p] += size[root_q];
                }
                else
                {
                    parent[root_p] = parent[root_q];
                    size[root_q] += size[root_p];
                }
                count--;
            }
        };

        bool connected(int p, int q)
        {
            int root_p = find(p);
            int root_q = find(q);
            return root_p == root_q;  
        };

        int count_num(void)
        {
            return count;
        };
};

void solve(vector<vector<int> >& nums)
{
    int m = nums.size();
    int n = nums[0].size();

    UnionFind uf(m*n+1);

    for(int i=0; i<n; i++)
    {
        if(nums[0][i] == 0)
            uf.union_pq(i, m*n);
        
        if(nums[m-1][i] == 0)
            uf.union_pq((m-1)*n+i, m*n);
    }
    
    for(int i=0; i<m; i++)
    {
        if(nums[i][0] == 0)
            uf.union_pq(i*n, m*n);
        
        if(nums[i][m-1] == 0)
            uf.union_pq(i*n+n-1, m*n);
    }

    int d[] = {1, 0, 0, 1, 0, -1, -1, 0,};

    for(int i=1; i<m-1; i++)
    {
        for(int j=1; j<n-1; j++)
        {   
            if(nums[i][j] == 0)
            int idx = i * m + j;
            if(uf.connected(idx, m*n))
        }
    }
}


int main()
{
    vector<vector<int> > nums(4, vector<int>(5, 1));
    nums[0][4] = 0;
    nums[1][3] = 0;
    nums[2][0] = 0;
    nums[2][1] = 0;
    nums[2][3] = 0;
    nums[3][1] = 0;

}