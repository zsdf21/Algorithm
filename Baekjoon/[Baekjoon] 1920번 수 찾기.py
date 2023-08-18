# 1920. 수 찾기
"""
N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 
이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

# 입력
첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 
다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 
다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 
이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.

# 출력
M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.
"""
import sys

N = int(sys.stdin.readline())
list_N = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
list_M = list(map(int, sys.stdin.readline().split()))

# ans1) for, list in으로 존재 여부 탐색 -> time error
ans = []
for i in list_M:
    if i in list_N:
        ans.append(1)
    else:
        ans.append(0)

print(*ans, sep='\n')

# for i in list_M:
#     if i in list_N:
#         print(1)
#     else:
#         print(0)


# ans2) 효율화 위해 list_N -> set 설정
N = int(sys.stdin.readline())
list_N = set(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
list_M = list(map(int, sys.stdin.readline().split()))

for i in list_M:
    if i in list_N:
        print(1)
    else:
        print(0)
        
# +) 이분 탐색도 하나의 아이디어가 될 수 있음.
## 중앙값 기준 크다 -> 절반 이상에서 탐색