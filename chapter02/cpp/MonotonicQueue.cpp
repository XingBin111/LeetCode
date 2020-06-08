#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <stdlib.h>
#include <list>

using namespace std;

class MontionicQueue
{   

    private:
        list<int> pq;
    public:
        void push(int x)
        {
            while(pq.size() > 0 && pq.back() < x)
                pq.pop_back();
            pq.push_back(x);
        }
        int max()
        {
            return *pq.begin();
        }

        void pop(int x)
        {
            if(pq.front() == x)
                pq.pop_front();
        }
        int size()
        {
            return pq.size();
        }
        void show_pq()
        {
             cout<<"listOne.begin()--- listOne.end():"<<endl;
            for (list<int>::iterator i = pq.begin(); i != pq.end(); ++i)
            cout << *i << " ";
            cout << endl;
        }
};

vector<int> max_slinding_window(int* nums, int k, int l)
{
    MontionicQueue dq;
    
    vector<int> v(l-k+1, 0);

    for(int i=0; i<l; i++)
    {
        if(i < k-1)
        {
            dq.push(nums[i]);
            // dq.show_pq();
        }
            
        else
        {   
            dq.push(nums[i]);
            v[i-k+1] = dq.max();
            dq.pop(nums[i-k]);
            
        }
    }
    return v;
};

int main()
{
    int nums[] = {1, 3, -1, -3, 5, 3, 6, 7};
    int l = sizeof(nums) / sizeof(nums[0]); 
    int k = 3;
    vector<int> v = max_slinding_window(nums, k, l);
    for(int i=0; i<v.size(); i++)
        cout << v[i] << endl;
    return 0;
}
