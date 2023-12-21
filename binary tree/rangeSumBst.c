//questao 938 leetcode 
//retornar a soma dos valores dos nos de uma arvore em que os valores esta dentro de um intervalo
int rangeSumBST(TNode *root, int low, int high) {
    if(root != NULL){
        if(root -> data >= low && root->data <= high){
            return root->val + rangeSumBST(root->left, low, high) + rangeSumBST(root->right, low, high);      
            
        }

        else if(root -> val > high){
            return rangeSumBST(root->left, low, high);
        }

        else if(root -> val < low){
            return rangeSumBST(root->right, low ,high);
        }
    }

    return 0;
}


