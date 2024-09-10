import sys
sys.stdin = open('input.txt', 'r')

def dfs(now):
    ans_dfs.append(now)
    visited[now] = 1

    for i in arr[now]:
        for j in arr[now][i]:
            if not visited[i][j]:
                dfs(i)

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# for i in range(n):
#     for j in range(len(arr[i])):
#         if arr[i][j]

visited = [0] * (n+1)
ans_dfs = []
dfs(0)