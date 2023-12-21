//questao 2331 leetcode

int evaluateTree(TNode* root) {
    if(root->l != NULL && root->r != NULL){
        if(root->data == 3){
            return evaluateTree(root->l) || evaluateTree(root->r);
        }
        else{
            return evaluateTree(root->l) && evaluateTree(root->r);
        }
    }

    else{
        if(root->data == 0){
            return FALSE;
        }

        else{
            return TRUE;
        }
    }
}
