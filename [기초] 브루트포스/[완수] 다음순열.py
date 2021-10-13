import sys
sys.stdin = open('input_files/다음순열.txt')
from itertools import permutations

# 메모리 초과
# N = int(input())
# numbers = list(map(int, input().split()))
# perms = sorted(list(permutations(numbers)))
#
# if list(perms[-1]) == numbers:
#     print(-1)
# else:
#     for i in range(len(perms)-1):
#         if list(perms[i]) == numbers:
#             print(*perms[i+1])
#             break


#
def dfs(idx):
    global ans
    if idx == N:
        ans.append(subset)
        print(ans)
        return ans

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            subset.append(numbers[i])
            dfs(idx+1)
            subset.pop()
            visited[i] = 0


N = int(input())
numbers = list(map(int, input().split()))
visited = [0] * N
subset = []
ans = []
if numbers == sorted(numbers, reverse=True):
    print(-1)
else:
    dfs(0)
print(ans)