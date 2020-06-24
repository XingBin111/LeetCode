#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include "limits.h"
#include <math.h>

using namespace std;

struct ListNode
{
    int val;
    ListNode* next;
    ListNode(int v=0, ListNode* nxt=nullptr) : val(v), next(nxt) {};
};

// 翻转整个链表
ListNode* reverse_list(ListNode* head)
{   
    if(head->next == nullptr)
        return head;
    ListNode* new_head = reverse_list(head->next);
    head->next->next = head;
    head->next = nullptr;
    return new_head;
}

// 翻转前k个节点
ListNode* reverse_list_k(ListNode* head, int k)
{
    if(head->next == nullptr || k == 1)
        return head;
    ListNode* new_head = reverse_list_k(head->next, k-1);
    ListNode* tmp_node = head->next->next;
    head->next->next = head;
    head->next = tmp_node;
    return new_head;
}

// 翻转[a, b)
ListNode* reverse_list_between(ListNode* a, ListNode* b)
{
    ListNode* pre = a;
    ListNode* cur = a->next;
    ListNode* nxt = nullptr;
    while(cur != b)
    {
        nxt = cur->next;
        cur->next = pre;
        pre = cur;
        cur = nxt;
    }
    return pre;
}

ListNode* reverse_list_group(ListNode* head, int k)
{   
    if(k == 1)
        return head;
    
    ListNode* a = head;
    ListNode* b = head;
    for(int i=0; i<k; i++)
    {
        if(b == nullptr)
            return a;
        b = b->next;
    }
    ListNode* new_head = reverse_list_between(a, b);
    a->next = reverse_list_group(b, k);
    return new_head;
}

void show(ListNode* head)
{
    ListNode* tmp = head;
    while(tmp != nullptr)
    {
        cout << tmp->val << endl;
        tmp = tmp->next;
    }
}

int main()
{
    ListNode* head = new ListNode(1);
    ListNode* tmp = head;
    for(int i=2; i<20; i++)
    {
        ListNode* tmp_node = new ListNode(i);
        tmp->next = tmp_node;
        tmp = tmp->next;
    }

    ListNode* new_head = reverse_list_group(head, 3);
    // head->next = nullptr;
    show(new_head);
    return 0;
}