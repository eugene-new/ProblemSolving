import sys

sys.stdin = open('input_files/암호만들기.txt')

L = 0
C = 0
alphabet_list = []
vowels = ['a', 'e', 'i', 'o', 'u']
password = []

visited = [False] * 16

def check_password():
    number_of_vowels = len(list(filter(lambda x : x in vowels, password)))
    number_of_consonants = len(password) - number_of_vowels

    if number_of_vowels >= 1 and number_of_consonants >= 2:
        return True
    else:
        return False

def dfs(start):
    global password
    if len(password) == L:
        if check_password():
            print(''.join(password))
        return

    for i in range(start, len(alphabet_list)):
        if visited[i] != True:
            visited[i] = True
            password.append(alphabet_list[i])
            dfs(i)
            visited[i] = False
            password.pop()


L, C = map(int, input().split())
alphabet_list = list(input().split())
alphabet_list.sort()

dfs(0)