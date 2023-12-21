//questao 700 leetcode 

// You are given the root of a binary search tree (BST) and an integer val.
// Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

TNode* searchBST(TNode* root, int val) {
    if(root != NULL){
        if(root->val == val){
            return root;
        }
        else if(root->val > val){
            return searchBST(root->left, val);
        }

        return searchBST(root->right, val);
    }

    return NULL;
}