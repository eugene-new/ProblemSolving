import sys
sys.stdin = open('input_files/숨바꼭질3.txt')
from collections import deque


def bfs(start, target):
    queue = deque([start])

    while queue:
        now = queue.popleft()

        if now == target:
            print(visited[now])
            return

        for i in (now*2, now-1, now+1):  # 순서 중요...! - 순서 다르게하면 틀림
            if 0 <= i < MAX and visited[i] == 0:
                if i == now*2:
                    visited[i] = visited[now]
                    queue.append(i)
                else:
                    visited[i] = visited[now] + 1
                    queue.append(i)


N, K = map(int, input().split())
MAX = 100001
visited = [0] * MAX
# bfs(N, K)
bfs(2, 1024)


# # 왜 위에껀 런타임 에러 나오고 아래껀 안나오는지...?
"""
1. for문의 순서
*2로 이동하는걸 가장 먼저하는건 당연합니다. 비용이 0이기 때문이죠
각 칸마다 비용을 비교하며 최신화 해도 되지만, 그럴필요가 없이, 2배 이동을 가장 먼저 해서 자리 잡아두는 용도로 생각해도 됩니다
그리고 -1이 +1보다 먼저 하는것은, -1 이동 후 *2 이동을 했을 때, 먼저 도착하는 경우가 있어서입니다
4 6 예시를 보면, 4 >> 3 >> 6 비용 1이 최소이지만, 더하기부터 넣는다면 4 >> 5 >> 6 비용 2가 나옵니다
"""

# from collections import deque
#
#
# def bfs():
#     q = deque([n])
#     while q:
#         x = q.popleft()
#         if x == k:
#             return array[x]
#         for nx in (x - 1, x + 1, 2 * x):
#             if 0 <= nx < MAX and not array[nx]:
#                 if nx == 2 * x and x != 0:
#                     array[nx] = array[x]
#                     q.appendleft(nx)  # 2*X 가 더 높은 우선순위를 가지기 위함
#                 else:
#                     array[nx] = array[x] + 1
#                     q.append(nx)
#
#
# MAX = 100001
# # n, k = map(int, input().split())
# n, k = 2, 1024
# array = [0] * MAX
# print(bfs())