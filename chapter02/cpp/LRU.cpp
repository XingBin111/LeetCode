#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <stdlib.h>
#include <unordered_map>

using namespace std;

struct ListNode
{
    int key;
    int val;
    ListNode* pre;
    ListNode* suc;

    ListNode(int _key=0, int _val=0, ListNode* _pre=nullptr, ListNode* _suc=nullptr) : key(_key), val(_val), pre(_pre), suc(_suc) {}
};

class DoubleList
{
    private:
        int dl_size;
        ListNode* head;
        ListNode* tail;
    
    public:
        DoubleList()
        {
            head = new ListNode();
            tail = new ListNode(0, 0, head);
            head->suc = tail;
            dl_size = 0;
        }

        void addFirst(ListNode* x)
        {
            ListNode* tmp = head->suc;
            head->suc = x;
            x->pre = head;

            x->suc = tmp;
            tmp->pre = x;
            dl_size++;
        }

        void remove(ListNode* x)
        {
            x->pre->suc = x->suc;
            x->suc->pre = x->pre;

            delete x;
            dl_size--;
        }

        vector<int> remove_last()
        {   
            if(dl_size > 0)
            {
                vector<int> v(2, 0);
                v[0] = tail->pre->key;
                v[1] = tail->pre->val;

                remove(tail->pre);
                return v;
            }
            
        }

        void show()
        {   
            ListNode* tmp = head->suc;
            while (tmp != tail)
            {
                cout << "key: " << tmp->key << ", val: " << tmp->val << endl;
                tmp = tmp->suc;
            }
            
        }

        ~DoubleList()
        {
            
            while(head->suc != tail)
            {
                remove(head->suc);
                dl_size--;
            }
            delete head;
            delete tail;
        }

};

void dl_usage()
{
    DoubleList dl;

    cout << "add (3, 4):\n";
    ListNode* x = new ListNode(3, 4);
    dl.addFirst(x);
    dl.show();

    cout << "add (1, 2):\n";
    dl.addFirst(new ListNode(1, 2));
    dl.show();

    cout << "add (5, 6):\n";
    dl.addFirst(new ListNode(5, 6));
    dl.show();

    cout << "remove last: \n";
    dl.remove_last();
    dl.show();
}

class LRUCache
{
    private:
        int cap;
        unordered_map<int, ListNode*> map;
        DoubleList dl;
    
    public:
        LRUCache(int _cap) : cap(_cap) {}

        void put(int key, int val)
        {
            ListNode* x = new ListNode(key, val);
            if(map.count(key))
            {
                dl.remove(map[key]);
                dl.addFirst(x);
                map[key] = x;
            }
            else
            {
                if(cap == map.size())
                {
                    int remove_key = dl.remove_last()[0];
                    map.erase(remove_key);
                }
                dl.addFirst(x);
                map[key] = x;
            }
        }

        int get(int key)
        {
            if(!map.count(key))
            {
                cout << "key not in map\n";
                return -1;
            }
                
            ListNode* x = map[key];
            put(x->key, x->val);
            return x->val;
        }

        void show()
        {
            dl.show();
        }

};

void lru_usage()
{
    LRUCache lru(3);
    lru.put(1, 2);
    lru.put(3, 4);
    lru.put(1, 3);
    cout << "lru show:\n";
    lru.show();

    lru.put(5, 6);
    lru.put(7, 8);

    cout << "lru show:\n";
    lru.show();

    cout << "lru show:\n";
    lru.get(5);
    lru.show();
}


int main()
{
    // dl_usage();
    lru_usage();
    return 0;
}