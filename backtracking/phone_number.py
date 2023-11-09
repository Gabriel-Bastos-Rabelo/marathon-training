
#leetcode 17

phone_dict = {2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4: ['g', 'h', 'i'], 5: ['j', 'k', 'l'], 6: ['m', 'n', 'o'], 7:['p', 'q', 'r', 's'], 8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z']}


def dfs(phone_dict, digits, current, res, index):
    if(len(current) == len(digits)):
        string = "".join(current)
        res.append(string)
        
    else:
        for i in phone_dict[int(digits[index])]:
            current.append(i)
            dfs(phone_dict, digits, current, res, index+1)
            current.pop()


    return res


print(dfs(phone_dict, "", [], [], 0))


