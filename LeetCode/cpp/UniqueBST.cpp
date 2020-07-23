#include <iostream>
#include <vector>
#include <stack>
#include <queue>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(NULL) {}
    ListNode(int x) : val(x), next(NULL) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(NULL), right(NULL) {}
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    vector<TreeNode*> generate(int start, int end)
    {
        vector<TreeNode*> res;
        for(int val=start; val<=end; val++)
        {
            vector<TreeNode*> left = generate(start, val-1);
            vector<TreeNode*> right = generate(val+1, end);
            for(int i=0; i<left.size(); i++)
            {
                for(int j=0; j<right.size(); j++)
                {
                    TreeNode* node = new TreeNode(val, left[i], right[j]);
                    res.push_back(node);
                }
            }
        }
        if(res.size() == 0)
            res.push_back(nullptr);
        return res;
    }


    vector<TreeNode*> generateTrees(int n)
    {
        vector<TreeNode*> res;
        if(n == 0)
            return res;
        return generate(1, n);
    }

};