import sys

sys.stdin = open('input_files/로또.txt')

k = 0
numbers = []
selected = []
visited = [False] * 14


def combination(start):
    if len(selected) == 6:
        output = " "
        print(output.join(selected))
        return

    for index in range(start, k):
        if visited[index] is False:
            visited[index] = True
            selected.append(numbers[index])
            combination(index)
            selected.pop()
            visited[index] = False



while True:
    input_string = input()
    if input_string == '0':
        break
    else:
        numbers = list(input_string.split())
        k = int(numbers[0])
        numbers = numbers[1:k+1]

    combination(0)
    print()


