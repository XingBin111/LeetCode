#include <iostream>
#include <list>

using namespace std;

struct ListNode{
	int val;
	ListNode* next;
    ListNode(int v=0) {val=v;}
};

class SlowFastPointer
{
    public:
        bool has_cycle(ListNode* head)
        {
            ListNode* fast = head;
            ListNode* slow = head;
            while(fast != NULL && fast->next != NULL)
            {
                fast = fast->next->next;
                slow = slow->next;
                if(fast == slow)
                    return true;
            }
            return false;
        }

        ListNode* detectCycle(ListNode* head)
        {
            ListNode* fast = head;
            ListNode* slow = head;
            while(fast != NULL && fast->next != NULL)
            {
                fast = fast->next->next;
                slow = slow->next;
                if(fast == slow)
                    break;
            }
            slow = head;
            while(slow != fast)
            {
                fast = fast->next;
                slow = slow->next;
            }
            return slow;
        }

        ListNode* reciprocal(ListNode* head)
        {
            ListNode* fast = head;
            ListNode* slow = head;
            while(fast != NULL && fast->next != NULL)
            {
                fast = fast->next->next;
                slow = slow->next;
            }
            return slow;
        }
};

void use_cycle()
{
    SlowFastPointer solution;
    ListNode* head = new ListNode();
    ListNode* node = head;
    for(int i=1; i<4; i++)
    {
        node->next = new ListNode(i);
        node = node->next;
    }

    cout << solution.has_cycle(head) << endl;
    ListNode* circle_node = node;
    for(int i=4; i<9; i++)
    {
        node->next = new ListNode(i);
        node = node->next;
    }
    node->next = circle_node;
    cout << solution.has_cycle(head) << endl;
    cout << solution.detectCycle(head)->val << endl;
}

void use_reciprocal()
{
    SlowFastPointer solution;
    ListNode* head = new ListNode();
    ListNode* node = head;
    for(int i=1; i<10; i++)
    {
        node->next = new ListNode(i);
        node = node->next;
    }
    cout << solution.reciprocal(head)->val << endl;
}

int main()
{
    use_cycle();
    use_reciprocal();
    return 0;
}
