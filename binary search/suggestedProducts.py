class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:       

        def binarySearch(products, inputChar):
            l = 0
            r = len(products) - 1

            while(l <= r):
                mid = l + (r - l)//2
                
                if(products[mid] < inputChar):
                    l = mid + 1

                else:
                    r = mid - 1

            return l

        
        products.sort()
        input_char = ""
        ans = []

        for i in searchWord:
            tmp = []
            input_char += i
            insertion_index = binarySearch(products, input_char)
            for i in range(insertion_index, min(len(products), insertion_index + 3)):
                if products[i].startswith(input_char):
                    tmp.append(products[i])

            ans.append(tmp)


        return ans
        