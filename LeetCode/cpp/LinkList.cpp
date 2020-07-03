#include <iostream>
#include <vector>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(NULL) {}
    ListNode(int x) : val(x), next(NULL) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class MyLinkedList {

    private:
        ListNode* header;
        int size;

    public:
        /** Initialize your data structure here. */
        MyLinkedList() {
            size = 0;
            header = new ListNode(0);
        }
        
        /** Get the value of the index-th node in the linked list. If the index is invalid, return -1. */
        int get(int index) {
            if(size < index)
                return -1;
            ListNode* head = header->next;
            for(int i=0; i<index; i++)
                head = head->next;
            return head->val;
        }
        
        /** Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list. */
        void addAtHead(int val) {
            ListNode* node = new ListNode(val, header->next);
            header->next = node;
            size++;
        }
        
        /** Append a node of value val to the last element of the linked list. */
        void addAtTail(int val) {
            ListNode* cur = header;
            ListNode* node = new ListNode(val);
            while(cur->next != nullptr)
                cur = cur->next;
            cur->next = node;
            size++;
        }
        
        /** Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted. */
        void addAtIndex(int index, int val) {
            if(size <= index)
                return;
            ListNode* node = new ListNode(val);
            ListNode* cur = header;
            for(int i=0; i<index; i++)
                cur = cur->next;
            node->next = cur->next;
            cur->next = node;
            size++;
        }
        
        /** Delete the index-th node in the linked list, if the index is valid. */
        void deleteAtIndex(int index) {
            if(index >= size)
                return;
            ListNode* cur = header;
            for(int i=0; i<index; i++)
                cur = cur->next;
            cur->next = cur->next->next;
            size--;
        }
        
        void show_list()
        {
            ListNode* cur = header->next;
            while(cur != nullptr)
            {
                cout << cur->val << endl;
                cur = cur->next;
            }
        }
};



int main()
{

    MyLinkedList* linkedList = new MyLinkedList(); // Initialize empty LinkedList
    linkedList->addAtHead(1);
    linkedList->addAtTail(3);

    linkedList->addAtIndex(1, 2);  // linked list becomes 1->2->3

    linkedList->show_list();

    cout << linkedList->get(1) << endl;            // returns 2
    linkedList->deleteAtIndex(1);  // now the linked list is 1->3

    linkedList->show_list();
    linkedList->get(1);            // returns 3
    return 0;
}