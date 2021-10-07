import sys
sys.stdin = open('input_files/일곱난쟁이.txt')

dwarfs = sorted(list(int(input()) for _ in range(9)))  # 난쟁이 키 오름차순 정렬
tot = sum(dwarfs)  # 아홉 난쟁이 키 총합

for i in range(8):
    for j in range(i+1, 9):
        # 난쟁이 2명의 키를 뺐을 때 나머지 일곱 난쟁이 키의 총합이 100이면 break
        if tot - (dwarfs[i]+dwarfs[j]) == 100:
            fake1 = dwarfs[i]  # 가짜 1
            fake2 = dwarfs[j]  # 가짜 2
            break
# 난쟁이 리스트에서 가짜 제거
dwarfs.remove(fake1)
dwarfs.remove(fake2)

for dwarf in dwarfs:
    print(dwarf)