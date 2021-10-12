import sys
sys.stdin = open('input_files/퇴사.txt')

N = int(input())
data = list(list(map(int, input().split())) for _ in range(N))
print(N, data)
dp = [0] * (N+1)

for i in range(N-1, -1, -1):
    if i + data[i][0] > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max((data[i][1] + dp[i+data[i][0]]), dp[i+1])

print(dp[0])