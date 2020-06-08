#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <stdlib.h>
#include <list>

using namespace std;

struct ListNode
{
    int val;
    ListNode* next;
    ListNode(int x, ListNode* _next=nullptr) { val = x; next = _next;}
};

void show_list(ListNode* head)
{
    ListNode* tmp = head;
    while(tmp != nullptr)
    {
        cout << tmp->val << endl;
        tmp = tmp->next;
    }
        
};

ListNode* reverse(ListNode* head)
{
    if(head->next == nullptr)
        return head;
    
    ListNode* last = reverse(head->next);
    head->next->next = head;
    head->next = nullptr;
    return last;
};

ListNode* reverse_iteration(ListNode* head)
{   
    if(head == nullptr && head->next == nullptr)
        return head;
    ListNode* pre = head;
    ListNode* cur = head->next;
    ListNode* nxt = head->next->next;

    pre->next = nullptr;

    while(nxt != nullptr)
    {
        cur->next = pre;
        pre = cur;
        cur = nxt;
        nxt = nxt->next;
    }
    cur->next = pre;
    return cur;
}

ListNode* succ = nullptr;
ListNode* reverseN(ListNode* head, int n)
{
    if(n == 1)
    {
        succ = head->next;
        return head;
    }
    ListNode* last = reverseN(head->next, n-1);
    head->next->next = head;
    head->next = succ;
    return last;
};

ListNode* reverse_between_mn(ListNode* head, int m, int n)
{
    if(m == 0)
        return reverseN(head, n);
    head->next = reverse_between_mn(head->next, m-1, n-1);
    return head;
};

int main()
{
    ListNode* head = new ListNode(0);
    ListNode* tmp = head;
    for(int i=1; i<8; i++)
    {
        tmp->next = new ListNode(i);
        tmp = tmp->next;
    }

    cout << "===========before reverse===========\n" ;
    show_list(head);

    cout << "===========after reverse===========\n" ;
    ListNode* new_head = reverse_between_mn(head, 2, 5);
    show_list(new_head);

    return 0;
}