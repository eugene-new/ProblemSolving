import sys

sys.stdin = open('input_files/일곱난쟁이.txt')

n = 9
heights = []
heightsOfMembers = []
visit = [False] * n
flag = False


def dfs(idx, count):
    global flag
    if flag is True:
        return
    elif count == 7:
        if sum(heightsOfMembers) == 100:
            flag = True
            for height in heightsOfMembers:
                print(height)
        return

    for index in range(idx, n):
        if visit[index] is False:
            visit[index] = True
            heightsOfMembers.append(heights[index])
            dfs(index, count + 1)
            visit[index] = False
            heightsOfMembers.pop()


for i in range(0, n):
    heights.append(int(input()))

heights.sort()
dfs(0, 0)
