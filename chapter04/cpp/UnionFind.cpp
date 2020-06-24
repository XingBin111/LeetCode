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

int main()
{
    UnionFind uf(10);
    uf.union_pq(1, 0);
    uf.union_pq(6, 0);
    uf.union_pq(3, 0);
    uf.union_pq(5, 2);
    uf.union_pq(5, 1);

    cout << uf.connected(5, 2) << endl;
    return 0;
}