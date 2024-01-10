

def binary_search():
    low = 1
    high = 1000000 
    numeroOp = 0

    while low < high:
        mid = (low + high + 1) // 2
        print(mid)
        s = input()
        numeroOp += 1

        if s == ">=":
            low = mid
        else:
            high = mid - 1

    print(f"! {low}")
    


binary_search()