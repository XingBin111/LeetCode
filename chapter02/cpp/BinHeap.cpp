#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <stdlib.h>

using namespace std;

/*    
最大二叉堆(也称优先级队列), 二叉堆其实就是完全二叉树, 但存在数组中, 把数组的索引当作指针
最大二叉堆性质: 父节点 >= 左右节点
插入和删除的时间复杂度为O(logN)
*/
class MaxPQ
{
public:
    vector<int> pq;
    MaxPQ(int cap=0) { pq = vector<int>(cap + 1); }
    // MaxPQ()                 {cout << "default constructor\n"; pq = vector<int>(1, 0);}
    int max() { return pq[1]; }

    // 静态操作
    bool less(int i, int j) { return pq[i] < pq[j]; }
    int parent(int root) { return root / 2; }
    int left(int root) { return root * 2; }
    int right(int root) { return root * 2 + 1; }
    int size() { return pq.size(); }
    void show() {
        cout << "element of pq:  ";
        for(int i=0; i<pq.size(); i++)
            cout << pq[i] << "    ";
        cout << endl;
    }

    // 动态操作
    void exchange(int i, int j) { swap(pq[i], pq[j]); }
    void insert(int e)
    {
        pq.push_back(e);
        swim(pq.size() - 1);
    }

    int del_max()
    {
        int max_elem = pq[1];
        exchange(1, pq.size() - 1);
        pq.pop_back();
        sink(1);
        return max_elem;
    }

    void swim(int k)
    {
        while (k > 1 && less(parent(k), k))
        {
            exchange(k, parent(k));
            k = parent(k);
        }
    }

    void sink(int k)
    {
        while (left(k) < pq.size())
        {
            int old_idx = left(k);
            if (right(k) < pq.size() && less(old_idx, right(k)))
                old_idx = right(k);
            if (less(old_idx, k))
                break;
            exchange(old_idx, k);
            k = old_idx;
        }
    }
};

int main()
{
    MaxPQ max_pq;
    int n = 10;
    int M = 100;
    for(int i=0; i<n; i++)
    {
        int insert_num = rand() % M + 1;
        cout << "insert: " << insert_num << endl;
        max_pq.insert(insert_num);
        max_pq.show();

    }

    for(int i=0; i<n; i++)
    {
        cout << "del max element of pq: " << max_pq.del_max() << endl;
        max_pq.show();
    }
    return 0;
}