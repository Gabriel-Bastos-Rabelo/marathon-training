#leetcode 1079

tiles = "AAB"
record = [0] * 26
for tile in tiles: record[ord(tile)-ord('A')] += 1
def dfs(record):
    s = 0
    for i in range(26):
        if not record[i]:
            continue
        print(chr(i + ord('A')))
        record[i] -= 1
        s += dfs(record) + 1
        record[i] += 1

    return s
    

dfs(record)
