#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <stdlib.h>
#include <unordered_map>

using namespace std;

struct TreeNode
{
    int val;
    TreeNode* lchild;
    TreeNode* rchild;

    TreeNode(int _val=0, TreeNode* l=nullptr, TreeNode* r=nullptr) : val(_val), lchild(l), rchild(r) {}
    bool is_leaf() {return lchild == nullptr && rchild == nullptr;}
};

void plus_one(TreeNode* x)
{
    if(x == nullptr)
        return;
    x->val++;
    plus_one(x->lchild);
    plus_one(x->rchild);
}

bool isSameTree(TreeNode* root1, TreeNode* root2)
{
    if(root1 == nullptr && root2 == nullptr)
        return true;
    
    if(root1 == nullptr && root2 == nullptr)
        return false;

    if(root1->val != root2->val)
        return false;
    return isSameTree(root1->lchild, root2->lchild) && isSameTree(root1->rchild, root2->rchild);
}

// 还是不太懂, 可以检查BST的中序遍历是否为单增的
bool isValidBST(TreeNode* root, TreeNode* min_node=nullptr, TreeNode* max_node=nullptr)
{
    if(root == nullptr) 
        return true;
    
    if(min_node != nullptr && min_node->val >= root->val) return false;
    if(max_node != nullptr && max_node->val <= root->val) return false;
    return isValidBST(root->lchild, min_node, root) && isValidBST(root->rchild, root, max_node);

}

bool isInBST(TreeNode* root, int target)
{
    if(root == nullptr) 
        return false;
    if(root->val == target)
        return true;
    
    if(root->val < target)
        return isInBST(root->rchild, target);
    else
        return isInBST(root->lchild, target);
}

// 这版本错误
// void insertIntoBSTI(TreeNode* root, int target)
// {
//     if(root->lchild == nullptr && root->val > target)
//         root->lchild = new TreeNode(target);
    
//     if(root->rchild == nullptr && root->val <target)
//         root->rchild = new TreeNode(target);
    
//     if(root->val < target)
//         insertIntoBSTI(root->rchild, target);
//     else    
//         insertIntoBSTI(root->lchild, target);
// }

TreeNode* insertIntoBST(TreeNode* root, int target)
{
    if(root == nullptr)
        return new TreeNode(target);
    
    if(root->val < target)
        root->rchild = insertIntoBST(root->rchild, target);
    if(root->val > target)
        root->lchild = insertIntoBST(root->lchild, target);
    return root;
}

// python版本更加优雅
TreeNode* deleteNode(TreeNode* root, int target)
{
    if(root->val == target)
    {
        if(root->rchild == nullptr)
        {   
            TreeNode* left_child = root->lchild;
            delete root;
            return left_child;
        }
        else
        {       
            TreeNode* tmp = root->rchild;
            while(tmp->lchild != nullptr)
                tmp = tmp->lchild;
            root->val = tmp->val;
            root->rchild = deleteNode(root->rchild, tmp->val);
            return root;
        }
    }
    
    if(root->val < target)
        root->rchild = deleteNode(root->rchild, target);
    
    if(root->val > target)
        root->lchild = deleteNode(root->lchild, target);
    return root;
}

void show_tree(TreeNode* root)
{
    if(root == nullptr)
        return;
    cout << root->val << endl;
    show_tree(root->lchild);
    show_tree(root->rchild);
}

int main()
{
    // TreeNode* root = new TreeNode(3);
    // root->lchild = new TreeNode(4);
    // root->rchild = new TreeNode(5);

    // root->lchild->rchild = new TreeNode(6);
    // root->lchild->lchild = new TreeNode(7);

    TreeNode* bst_root = new TreeNode(8);
    bst_root->lchild = new TreeNode(4);
    bst_root->rchild = new TreeNode(20);

    bst_root->lchild->rchild = new TreeNode(6);
    bst_root->rchild->lchild = new TreeNode(15);

    bst_root->rchild->lchild->lchild = new TreeNode(9);
    bst_root->rchild->lchild->rchild = new TreeNode(16);

    bst_root->rchild->rchild = new TreeNode(30);
    bst_root->rchild->rchild->lchild = new TreeNode(25);
    bst_root->rchild->rchild->rchild = new TreeNode(33);
    show_tree(bst_root);

    // cout << "insert: 9" << endl;    
    // bst_root = insertIntoBST(bst_root, 9);
    int n = 9;
    cout << "delete: " << n << endl;  
    bst_root = deleteNode(bst_root, n);
    show_tree(bst_root);

    return 0;

}
