import sys
sys.stdin = open('input_files/집합.txt')


# pypy3로 돌릴 때 메모리 초과
def add(x):
    global S
    if x in S:
        return
    S.add(x)


def remove(x):
    global S
    if x not in S:
        return
    S.remove(x)


def check(x):
    global S
    if x in S:
        print(1)
    else:
        print(0)


def toggle(x):
    global S
    if x in S:
        S.remove(x)
    else:
        S.add(x)


M = int(input())
S = set()

for _ in range(M):
    tmp = sys.stdin.readline().rsplit()
    if tmp[0] == 'all':
        S = set(range(1, 21))
    elif tmp[0] == 'empty':
        S.clear()
    elif tmp[0] == 'add':
        add(int(tmp[1]))
    elif tmp[0] == 'remove':
        remove(int(tmp[1]))
    elif tmp[0] == 'toggle':
        toggle(int(tmp[1]))
    elif tmp[0] == 'check':
        check(int(tmp[1]))



# 시간초과, 메모리 초과
# import sys
# sys.stdin = open('input_files/집합.txt')
#
#
# def func(definition, number):
#     if definition == 'add':
#         add(number)
#     if definition == 'remove':
#         remove(number)
#     if definition == 'check':
#         check(number)
#     if definition == 'toggle':
#         toggle(number)
#
#
# def add(x):
#     global S
#     if x in S:
#         return
#     S.add(x)
#
#
# def remove(x):
#     global S
#     if x not in S:
#         return
#     S.remove(x)
#
#
# def check(x):
#     global S
#     if x in S:
#         print(1)
#     else:
#         print(0)
#
#
# def toggle(x):
#     global S
#     if x in S:
#         S.remove(x)
#     else:
#         S.add(x)
#
#
# M = int(input())
# S = set()
#
# for _ in range(M):
#     tmp = input().split()
#     if tmp[0] == 'all':
#         definition = 'all'  # defitition 명시
#         S = set(i for i in range(1, 21))
#     elif tmp[0] == 'empty':
#         definition = 'empty'  # definition 명시
#         S = set()
#     else:
#         definition = tmp[0]
#         number = int(tmp[1])
#     func(definition, number)
