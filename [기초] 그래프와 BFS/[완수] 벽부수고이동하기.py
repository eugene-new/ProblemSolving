import sys
sys.stdin = open('input_files/ 벽부수고이동하기.txt')
from collections import deque

# 우, 하, 좌, 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]




N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
