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
 
struct DoublyListNode {
    int val;
    DoublyListNode *next, *prev;
    DoublyListNode(int x) : val(x), next(NULL), prev(NULL) {}
};

class Solution {
public:
    int search(const vector<int>& vec, int val)
    {
        for(int i=0; i<vec.size(); i++)
        {
            if(vec[i] == val)
                return i;
        }
        return vec.size();
    }
    
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        int n = inorder.size();
        TreeNode* root = new TreeNode(postorder[n-1]);
        if(n == 1)
            return root;
        int idx = search(inorder, root->val);
        vector<int> inorder_left_vec(inorder.begin(), inorder.begin()+idx);
        vector<int> inorder_right_vec(inorder.begin()+idx+1, inorder.end());
        
        vector<int> postorder_left_vec(postorder.begin(), postorder.begin()+idx);
        vector<int> postorder_right_vec(postorder.begin()+idx, postorder.end()-1);
        
        root->left = buildTree(inorder_left_vec, postorder_left_vec);
        root->right = buildTree(inorder_right_vec, postorder_right_vec);
        return root;
    }
};

void show_tree(TreeNode* root)
{
    queue<TreeNode*> q;
    q.push(root);
    while(!q.empty())
    {
        TreeNode* cur = q.front();
        q.pop();

        cout << cur->val << endl;
        if(cur->left)   q.push(cur->left);
        if(cur->right)  q.push(cur->right);
    }
}

int main()
{   
    Solution s;
    int a[5] = {9,3,15,20,7};
    int b[5] = {9,15,7,20,3};
    vector<int> arr;
    vector<int> res;
    for(int i=0; i<5; i++)
    {
        arr.push_back(a[i]);
        res.push_back(b[i]);
    }
    // TreeNode* root = new TreeNode(1);
    // TreeNode* tmp = root;
    // tmp->right = new TreeNode(2);
    // tmp->right->left = new TreeNode(3);
    TreeNode* root = s.buildTree(arr, res);
    show_tree(root);
    // while (k != NULL)
    // {
    //     cout << k->val << endl;
    //     k = k->next;
    // }
    
    // for(int i=0; i < res.size(); i++)
    //     cout << res[i] << endl;
    return 0;
}