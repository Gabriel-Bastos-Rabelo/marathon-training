from typing import List
import sys

# Suponha que N é definido com um valor alto suficiente para lidar com os casos de teste.
N = 200 * 1000 + 11

def dfs(v: int, g: List[List[int]], used: List[bool], comp: List[int]) -> None:
    used[v] = True
    comp.append(v)
    
    for to in g[v]:
        if not used[to]:
            dfs(to, g, used, comp)

def main() -> None:
    # Substituir por sys.stdin.readline().strip() se quiser ler de um arquivo ou entrada padrão
    n, m = map(int, input().split())
    deg = [0] * n
    used = [False] * n
    g = [[] for _ in range(n)]
    
    for _ in range(m):
        x, y = map(int, input().split())
        x, y = x - 1, y - 1
        g[x].append(y)
        g[y].append(x)
        deg[x] += 1
        deg[y] += 1
    
    ans = 0
    for i in range(n):
        if not used[i]:
            comp = []
            dfs(i, g, used, comp)
            ok = all(deg[v] == 2 for v in comp)
            if ok:
                ans += 1
    
    print(ans)

if __name__ == "__main__":
    main()
