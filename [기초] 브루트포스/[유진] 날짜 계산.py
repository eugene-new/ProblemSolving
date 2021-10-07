import sys

sys.stdin = open('input_files/날짜계산.txt')

earth, sun, moon = map(int, input().split())

answer = -1


def check(year, number, planet):
    if (year - planet) % number == 0:
        return True
    else:
        return False


for year in range(1, 7981):
    if check(year, 15, earth) and check(year, 28, sun) and check(year, 19, moon):
        answer = year

print(answer)