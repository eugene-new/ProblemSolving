import sys
sys.stdin = open('input_files/암호만들기.txt')
from itertools import combinations


def vowel_count(tup):  # 모음 갯수 구하는 함수
    cnt = 0
    for i in tup:
        if i in vowel:
            cnt += 1
    return cnt


def dfs(idx):  # DFS로도 풀어봄
    if idx == L:
        if 1 <= vowel_count(subset) <= L-2:
            print(''.join(subset))

    for i in range(idx, C):
        if visited[i] == 0:
            visited[i] = 1
            subset.append(chars[i])
            dfs(idx+1)
            subset.pop()
            visited[i] = 0


L, C = map(int, input().split())
chars = sorted(list(map(str, input().split())))  # 알파벳 오름차순 정렬
vowel = ['a', 'e', 'i', 'o', 'u']  # 모음

pw_lst = list(combinations(chars, L))  # 가능한 암호 조합을 tuple 형식으로 받은 list 제작
print(pw_lst)
for pw in pw_lst:
    if 1 <= vowel_count(pw) <= L-2:  # 최소 한 개의 모음, 최소 두 개의 자음으로 구성된 암호
        print(''.join(pw))


subset = []
visited = [0] * C
# dfs(0)