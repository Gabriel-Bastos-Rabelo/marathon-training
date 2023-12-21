//questao 226 leetcode
//Given the root of a binary tree, invert the tree, and return its root.

TNode* invertTree(TNode* root) {
    if(root != NULL){
        TNode* temp = root->l;
        root->l = invertTree(root->r);
        root->r = invertTree(temp);

        return root;
    }

    else{
        return NULL;
    }
}
