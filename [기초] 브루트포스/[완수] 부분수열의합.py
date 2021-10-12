import sys
sys.stdin = open('input_files/부분수열의합.txt')


# powerset 확인하는 함수
def dfs(idx):
    global cnt
    if idx == N:
        if subset != [] and sum(subset) == S:  # 크기가 양수인 부분수열 + 원소 합이 S
            cnt += 1
        return

    subset.append(numbers[idx])
    dfs(idx+1)

    subset.pop()
    dfs(idx+1)


N, S = map(int, input().split())
numbers = list(map(int, input().split()))

subset = []
cnt = 0
dfs(0)
print(cnt)