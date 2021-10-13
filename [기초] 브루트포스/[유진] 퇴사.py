import sys

sys.stdin = open('input_files/퇴사.txt')

N = 0
term = []
price = []

# memo = [i상담][true/false]
memo = [-1] * 20


def dp(day):
    if day == N:
        return 0
    elif day > N:
        return -1500000
    elif memo[day] != -1:
        return memo[day]

    memo[day] = max(dp(day + 1), price[day] + dp(day + term[day]))
    return memo[day]


N = int(input())
for i in range(0, N):
    t, p = map(int, input().split())
    term.append(t)
    price.append(p)

dp(0)

print(memo[0])