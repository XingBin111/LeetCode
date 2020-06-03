#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <unordered_map>

using namespace std;

class TreeNode{
public:
    int data;
    struct TreeNode *lchild,*rchild;
    TreeNode(int _data=0, TreeNode* _lchild=NULL, TreeNode* _rchild=NULL) : data(_data), lchild(_lchild), rchild(_rchild) {}
};

int rob1(const vector<int>& nums)
{
    if(nums.size() < 3)
        return *max_element(nums.begin(), nums.end());

    vector<int> dp_table(nums.begin(), nums.end());

    for(int i=2; i<nums.size(); i++)
        dp_table[i] = max({dp_table[i-2]+nums[i], dp_table[i-1]});
    
    return dp_table[nums.size()-1];
}

// 只与前面2个状态有关, 所以可以优化
int rob1_optimized(const vector<int>& nums)
{
    if(nums.size() < 3)
        return *max_element(nums.begin(), nums.end());

    int pre_pre = nums[0];
    int pre = nums[1];
    int res;
    for(int i=2; i<nums.size(); i++)
    {
        res = max({pre_pre + nums[i], pre});
        pre_pre = pre;
        pre = res;
    }
    return res;
}

int rob2(const vector<int>& nums)
{
    if(nums.size() < 3)
        return *max_element(nums.begin(), nums.end());
    else
    {
        return max({
            rob1_optimized(vector<int>(nums.begin(), nums.end()-1)),
            rob1_optimized(vector<int>(nums.begin()+1, nums.end())),
        });
    }
    
}

// 还可以用dp_table优化
int rob3(TreeNode* head)
{
    if(head == NULL)
        return 0;
    
    TreeNode* right = head->rchild;
    TreeNode* left = head->lchild;

    int rob_left_left=0, rob_left_right=0;
    int rob_right_left=0, rob_right_right=0;
    int res;

    if(left != NULL)
    {
        rob_left_left = rob3(left->lchild);
        rob_left_right = rob3(left->rchild);
    }

    if(right != NULL)
    {
        rob_right_left = rob3(right->lchild);
        rob_right_right = rob3(right->rchild);
    }

    res = max({
        head->data+rob_right_right+rob_right_left+rob_left_left+rob_left_right,
        rob3(head->lchild) + rob3(head->rchild)
    });
    return res;
    
}

int main()
{
    vector<int> nums = {1, 2, 3, 1};
    cout << rob2(nums) << endl;

    TreeNode* head = new TreeNode(3);
    head->lchild = new TreeNode(2);
    head->rchild = new TreeNode(3);

    
    head->lchild->rchild = new TreeNode(3);
    head->rchild->rchild = new TreeNode(1);

    cout << rob3(head) << endl;

    return 0;

}