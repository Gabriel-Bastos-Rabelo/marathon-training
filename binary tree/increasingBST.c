//questao 897 leetcode
// Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the 
// root of the tree, and every node has no left child and only one right child.

TNode* increasingBST(TNode* root, TNode *tail) {
    if(root != NULL){
        TNode *res = increasingBST(root->l, root);
        root->l = NULL;
        root->r = increasingBST(root->right, tail);

        return res;
    }
    else{
        return tail;
    }

}