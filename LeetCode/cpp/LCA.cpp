#include <iostream>
#include <vector>
#include <stack>
#include <queue>

using namespace std;

struct ListNode{
    int val;
    ListNode *next;
    ListNode(int x) : val(0), next(nullptr) {}
    ListNode(int x, ListNode *node) : val(x), next(node) {}
};

struct TreeNode{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *_left, TreeNode *_right) : val(x), left(_right), right(_right) {}
};


// struct ListNode {
//     int val;
//     ListNode *next;
//     ListNode() : val(0), next(NULL) {}
//     ListNode(int x) : val(x), next(NULL) {}
//     ListNode(int x, ListNode *next) : val(x), next(next) {}
// };

// struct TreeNode {
//     int val;
//     TreeNode *left;
//     TreeNode *right;
//     TreeNode() : val(0), left(NULL), right(NULL) {}
//     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
//     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
// };


class Solution{
    public:
        TreeNode* lowestCommonAncestor(TreeNode *root, TreeNode *p, TreeNode *q){
            if (root == nullptr)
                return nullptr;
            
            if (root == p || root == q)
                return root;

            TreeNode *left = lowestCommonAncestor(root->left, p, q);
            TreeNode *right = lowestCommonAncestor(root->right, p, q);

            if (left != nullptr && right != nullptr)
                return root;
                        
            return (left != nullptr) ? left : right;
        }
};


// // 递归寻找最低公共祖先
// class Solution {
// public:
   
//     TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
//         if(root == nullptr)
//             return nullptr;
//         if(root == p || root == q)
//             return root;
        
//         TreeNode* left = lowestCommonAncestor(root->left, p, q);
//         TreeNode* right = lowestCommonAncestor(root->right, p, q);
        
//         if(left != nullptr && right != nullptr)
//             return root;
//         return (left != nullptr) ? left : right;
//     }
// };