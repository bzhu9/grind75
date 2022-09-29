/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        int minVal = min(p->val, q->val);
        int maxVal = max(p->val, q->val);
        while (root) {
            if (minVal <= root->val && maxVal >= root->val)
                return root;
            else if (maxVal < root->val)
                root = root->left;
            else
                root = root->right;
        }
        return NULL;
    }
};
