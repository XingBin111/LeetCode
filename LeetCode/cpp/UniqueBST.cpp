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