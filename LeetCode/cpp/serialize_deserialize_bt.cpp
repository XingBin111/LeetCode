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

class Codec {
public:

    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        if(root == nullptr)
            return "N";
        string left = "," + serialize(root->left);
        string right = "," + serialize(root->right);
        return to_string(root->val) + left + right;
    }

    // Decodes your encoded data to tree.
    TreeNode *DShelper(string data,int &index){
        if(index >= data.size())
            return NULL;
        if(data[index] == 'N'){
            index += 2;
            return NULL;
        }
        string s = "";
        while(index < data.size() && data[index] != ','){
            s += data[index];
            index++;
        }
        index++;
        if(s == "")
            return NULL;
        int x = stoi(s);
        TreeNode *root = new TreeNode(x);
        root->left = DShelper(data,index);
        root->right = DShelper(data,index);
        return root;
    }
    TreeNode* deserialize(string s) {
        int index = 0;
        return DShelper(s,index);
    }
};