import sys
sys.stdin = open('input_files/연결요소의개수.txt')

# N, M = map(int, input().split())
# graph = [[] for _ in range(N+1)]
#
#
# # 런타임 에러
# def dfs(v):
#     global lst
#     lst.append(v)
#     visited[v] = True
#
#     for i in graph[v]:
#         if visited[i] == False:
#             dfs(i)
#
#
# for _ in range(M):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)
#
# ans = set()
# for i in range(1, N):
#     lst = []
#     visited = [False] * 1001
#     dfs(i)
#     ans.add(tuple(sorted(lst)))
#
# print(len(ans))


# python으로 돌리면 시간초과 / pypy3으로 돌리면 시간초과 안나옴
import sys
sys.setrecursionlimit(10000)  # 재귀제한이 걸려있어 허용치가 넘어가면 런타임 에러 _ 방지용

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
cnt = 0


# visited 리스트 변화
def dfs(v):
    visited[v] = True

    for i in graph[v]:
        if visited[i] == False:
            dfs(i)


for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 1부터 시작해서 연결 요소 여부 확인
for j in range(1, N+1):
    if visited[j] == False:
        dfs(j)
        cnt += 1

print(cnt)