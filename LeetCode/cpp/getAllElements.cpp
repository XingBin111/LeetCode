#include <iostream>
#include <vector>
#include <stack>
#include <queue>

using namespace std;

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
    void go_left(TreeNode* x, stack<TreeNode*>& st){
        while(x){
            st.push(x);
            x = x->left;
            
        }
    }
    
    vector<int> mid_traverse(TreeNode* root)
    {
        vector<int> res;
        stack<TreeNode*> st;
        
        TreeNode* x = root;
        while(true){
            go_left(x, st);
            if(st.empty())
                break;
            x = st.top();
            st.pop();
            res.push_back(x->val);
            x = x->right;
        }
        return res;
        
    }
    
    void merge(vector<int>& res, vector<int>& res1, vector<int>& res2){
        int i = 0, j = 0;
        int m = res1.size(), n = res2.size();
        while(i < m || j < n){
            if(i == m){
                res[i+j] = res2[j];
                j++;
            }
                
            else if(j == n){
                res[i+j] = res1[i];
                i++;
            }
                
            else if(res1[i] > res2[j]){
                res[i+j] = res2[j];
                j++;
            }
                
            else{
                res[i+j] = res1[i];
                i++;
            }
                
        }
    }
    
    vector<int> getAllElements(TreeNode* root1, TreeNode* root2) {
        vector<int> res1 = mid_traverse(root1);
        vector<int> res2 = mid_traverse(root2);
        vector<int> res(res1.size()+res2.size(), 0);
        merge(res, res1, res2);
        return res;
    }
};

int main(){
TreeNode* bst_root = new TreeNode(2);
    bst_root->left = new TreeNode(1);
    bst_root->right = new TreeNode(4);

    // TreeNode* bst_root = new TreeNode(8);
    // bst_root->left = new TreeNode(4);
    // bst_root->right = new TreeNode(20);

    // bst_root->left->right = new TreeNode(6);
    // bst_root->right->left = new TreeNode(15);

    // bst_root->right->left->left = new TreeNode(9);
    // bst_root->right->left->right = new TreeNode(16);

    // bst_root->right->right = new TreeNode(30);
    // bst_root->right->right->left = new TreeNode(25);
    // bst_root->right->right->right = new TreeNode(33);

    TreeNode* bst_root1 = new TreeNode(1);
    bst_root1->left = new TreeNode(0);
    bst_root1->right = new TreeNode(3);

    // bst_root1->left->right = new TreeNode(6);
    // bst_root1->right->left = new TreeNode(15);

    // bst_root1->right->left->left = new TreeNode(9);
    // bst_root1->right->left->right = new TreeNode(16);

    // bst_root1->right->right = new TreeNode(30);
    // bst_root1->right->right->left = new TreeNode(25);
    // bst_root1->right->right->right = new TreeNode(33);

    Solution s;
    vector<int> res = s.getAllElements(bst_root, bst_root1);
    for(auto& x: res)
        cout << x << endl;
    return 0;
}