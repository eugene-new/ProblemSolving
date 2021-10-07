import sys
sys.stdin = open('input_files/1,2,3더하기.txt')


def func(num):
    if num == 1:  # 1
        return 1
    if num == 2:  # (1, 1),  (2)
        return 2
    if num == 3:  # (1, 1, 1), (1, 2), (1, 2), (3)
        return 4
    else:
        return func(num-1) + func(num-2) + func(num-3)


T = int(input())
for _ in range(T):
    n = int(input())
    print(func(n))
