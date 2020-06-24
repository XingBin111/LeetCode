#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include "limits.h"
#include <math.h>
#include <stdlib.h>

using namespace std;

struct ListNode
{
    int val;
    ListNode* next;
    ListNode(int v=0, ListNode* nxt=nullptr) : val(v), next(nxt) {};
};

int get_random(ListNode* head)
{   
    srand((unsigned)time(NULL)); 
    ListNode* node = head->next;
    int choice = head->val;
    int k = 2;
    while(node != nullptr)
    {
        int r = rand() % k;
        cout << r << endl;
        if(r == 0)
            choice = node->val;

        node = node->next;
        k++;
    }
    return choice;
}

int main()
{
    ListNode* head = new ListNode(1);
    ListNode* tmp = head;

    for(int i=2; i<20; i++)
    {
        tmp->next = new ListNode(i);
        tmp = tmp->next;
    }

    cout << get_random(head) << endl;
    return 0;
}