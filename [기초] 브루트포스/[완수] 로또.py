import sys
sys.stdin = open('input_files/로또.txt')
from itertools import permutations


while True:
    lst = list(map(int, input().split()))
    k = lst[0]
    if k == 0:
        break

    s = lst[1:]
    numbers = []
    for perm in permutations(s, 6):
        numbers.append(sorted(list(perm)))

    numbers = list(set([tuple(set(number)) for number in numbers]))
    new = []
    for number in numbers:
        new.append(list(number))

    for i in new:
        i.sort()

    new = sorted(new, key=lambda x:x[0])
    for i in new:
        print(*i)
    print()

