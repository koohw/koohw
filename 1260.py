# 백준 24479. 알고리즘 수업 - 깊이 우선 탐색 1

# 1. N개의 정점, M개의 간선으로 구성된 무방향 그래프
# 정점 번호 1~N번
# 모든 간선의 가중치는 1 -> 양방향
# 정점 R에서 시작하여 dfs로 노드를 방문할 경우 노드의 방문 순서 출력
# 인접 정점은 오름차순으로 방문

def dfs(now):
    ans_dfs.append(now)
    visited[now] = 1

    for next in arr[now]:
        if not visited[next]:
            dfs(next)


N, M, R = map(int, input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    start, node = map(int, input().split())
    arr[start].append(node)
    arr[node].append(start)

for i in range(1, N+1):
    arr[i].sort()

visited = [0] * (N+1)
ans_dfs = []
dfs(R)

for j in ans_dfs:
    print(j)