//questao 1379 leetcode
// Given two binary trees original and cloned and given a reference to a node target in the original tree.

// The cloned tree is a copy of the original tree.

// Return a reference to the same node in the cloned tree.

// Note that you are not allowed to change any of the two trees or the target node and the answer must be a reference to a node in the cloned tree.

TNode* getTargetCopy(TNode* original, TNode* cloned, TNode* target) {
        if(original != NULL && cloned != NULL){
            if(original->data == target->data && cloned->data == target -> data){
                return cloned;
            }

            else{
                possibilidade1 = getTargetCopy(original->l, cloned->l, target);
                if(possibilidade1 != NULL){
                    return possibilidade1;
                }
                possibilidade2 = getTargetCopy(original->r, cloned->r, target);
                if(possibilidade2 != NULL){
                    return possibilidade2;
                }

                return NULL;

                
            }
        }

        return NULL;
}
