# 백준 1260. DFS와 BFS

# 1. 그래프 DFS 결과, BFS 결과 출력
# 2. 방문가능한 정점이 여러개인 경우 정점번호가 작은 것 먼저 방문
# 3. 더 이상 방문할 점이 없는 경우 종료
# 정점번호는 1~N
# N: 정점개수, M: 간선 개수
# V: 탐색 시작할 정점 번호
# 간선은 양방향
import sys
sys.stdin = open('input.txt', 'r')

def dfs(now):
    ans_dfs.append(now) # 방문 노드 추가
    v[now] = 1          # 방문 표시

    for next in adj[now]:
        if not v[next]: # 아직 방문하지 않은 노드인 경우
            dfs(next)

def bfs(start):
    q = []              # 필요한 q, v[], 변수 생성

    q.append(start)     # q에 초기데이터(들) 삽입
    ans_bfs.append(start)
    v[start] = 1

    while q:            # q에 데이터가 있는 동안
        now = q.pop(0)
        for next in adj[now]:
            if not v[next]: # 방문하지 않은 노드 -> 큐 삽입
                q.append(next)
                ans_bfs.append(next)
                v[next] = 1



N, M, V = map(int, input().split())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)    # 양방향

# [1] 오름차순 정렬
for i in range(1, N+1):
    adj[i].sort()

v = [0] * (N+1)
ans_dfs = []
dfs(V)

v = [0] * (N+1)
ans_bfs = []
bfs(V)

print(*ans_dfs)
print(*ans_bfs)