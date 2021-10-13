import sys

sys.stdin = open('input_files/집합.txt')

set = []


def add(x):
    if x not in set:
        set.append(x)


def remove(x):
    if x in set:
        set.remove(x)


def check(x):
    if x in set:
        print(1)
    else:
        print(0)


def toggle(x):
    if x in set:
        set.remove(x)
    else:
        set.append(x)


def all():
    set.clear()
    for i in range(1, 21):
        set.append(i)


def empty():
    set.clear()


M = int(input())
for i in range(0, M):
    tmp = sys.stdin.readline().rsplit()
    op = tmp[0]

    if op == 'add':
        add(int(tmp[1]))
    elif op == 'remove':
        remove(int(tmp[1]))
    elif op == 'check':
        check(int(tmp[1]))
    elif op == 'toggle':
        toggle(int(tmp[1]))
    elif op == 'all':
        all()
    elif op == 'empty':
        empty()
