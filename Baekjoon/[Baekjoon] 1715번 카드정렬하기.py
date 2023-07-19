# 1715 카드 정렬하기
# 첫째 줄 N, N개의 줄에 걸쳐 카드 묶음 크기 나열

import sys
import heapq

N = int(input())
card_list = []

# A1. 리스트 input append(N개) -> sorting -> (a+b)*N-1 + c*(N-2) ...
## 리스트 큰 순 정렬 -> i 순차 곱의 총합(if i==n : *i-1)
## Error) 10, 10, 10, 10일 때 -> 순차가 아닌 (10, 10) (10, 10) -> (20, 20)이 최적인데 이를 고려 X
## list 구조 활용 시 비교 후 다시 리스트에 넣고 정렬하는 과정을 거쳐야 할 듯.

# for _ in range(N):
#     card_list.append(int(input()))

# card_list = sorted(card_list, reverse=True)
# # card_list.sort(reverse=True)
# print(card_list)

# count=0
# # if N >= 2:
# for i in range(N):
#     if (i+1) != N:
#         count += card_list[i]*(i+1)
#     # 가장 작은 수는 i번만큼 사용됨. 
#     else:
#         count += card_list[i]*(i)
# # else: count=0

# print(count)

# A2. heapq 활용
## heapq: 
for _ in range(N):
    heapq.heappush(card_list, int(input()))# int(input('new input:')))
    # print(card_list)
    
count = 0

while len(card_list) > 1:
    a = heapq.heappop(card_list)
    b = heapq.heappop(card_list)
    count += a+b

    heapq.heappush(card_list, a+b)

print(count)