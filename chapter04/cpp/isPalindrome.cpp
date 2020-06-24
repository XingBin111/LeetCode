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

ListNode* reverse(ListNode* head)
{
    if(head->next == nullptr)
        return head;
    ListNode* new_head = reverse(head->next);
    head->next->next = head;
    head->next = nullptr;
    return new_head;
}

bool is_palindrome(ListNode* head)
{
    ListNode* slow = head;
    ListNode* fast = head;

    while(fast!= nullptr && fast->next != nullptr)
    {
        slow = slow->next;
        fast = fast->next->next;
    }
    if(fast != nullptr)
        slow = slow->next;
    ListNode* new_head = reverse(slow);

    while(new_head != nullptr)
    {
        if(new_head->val != head->val)
            return false;
        else
        {
            new_head = new_head->next;
            head = head->next;
        }
    }
    return true;
}

int main()
{
    ListNode* head = new ListNode(1);
    ListNode* tmp = head;

    tmp->next = new ListNode(2);
    tmp = tmp->next;

    tmp->next = new ListNode(3);
    tmp = tmp->next;

    tmp->next = new ListNode(2);
    tmp = tmp->next;

    tmp->next = new ListNode(2);
    tmp = tmp->next;

    cout << is_palindrome(head) << endl;
    return 0;
}
