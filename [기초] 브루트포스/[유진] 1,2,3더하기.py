import sys

sys.stdin = open('input_files/1,2,3더하기')

target = 0
numbers = [1, 2, 3]
answer = 0

def permutation(sum):
    global answer
    if sum == target:
        answer = answer + 1
        return

    for i in range(0, len(numbers)):
        nsum = sum + numbers[i]
        if nsum <= target:
            permutation(nsum)


T = int(input())
for tc in range(0, T):
    target = int(input())
    permutation(0)
    print(answer)
    answer = 0