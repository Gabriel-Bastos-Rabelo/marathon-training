//questao 104
// Given the root of a binary tree, return its maximum depth.
// A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

int maxDepth(TNode* root) {
    if(root != NULL){
        int rightPath = 1 + maxDepth(root->r);
        int leftPath = 1 + maxDepth(root -> l);

        if(rightPath >= leftPath){
            return rightPath;
        }

        else{
            return leftPath;
        }
    }
    return 0;
}