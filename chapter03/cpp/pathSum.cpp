#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <stdlib.h>

using namespace std;

struct TreeNode
{
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int _val=0, TreeNode* _left=nullptr, TreeNode* _right=nullptr) : val(_val), left(_left), right(_right) {}
};

int path_sum_helper(TreeNode* root, int target)
{
    if(root == nullptr)
        return 0;

    return (target == root->val) + path_sum_helper(root->left, target-root->val) + path_sum_helper(root->right, target-root->val);
}

int path_sum(TreeNode* root, int target)
{   
    if(root == nullptr)
        return 0;
    
    return path_sum_helper(root, target) + path_sum(root->left, target) + path_sum(root->right, target);
    
}


int main()
{
    TreeNode* root = new TreeNode(10);
    root->left = new TreeNode(5);
    root->right = new TreeNode(-3);

    root->left->left = new TreeNode(3);
    root->left->right = new TreeNode(2);

    root->right->right = new TreeNode(11);

    root->left->left->left = new TreeNode(3);
    root->left->left->right = new TreeNode(-2);

    root->left->right->right = new TreeNode(1);

    int target = 8;
    cout << path_sum(root, target) << endl;
    return 0;
}