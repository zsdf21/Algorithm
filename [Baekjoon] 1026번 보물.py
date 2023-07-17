# 1026 보물(1<=N<=50) (0 <= A[i] and B[i] <= 100)
## A1. list A, B를 각 내림 및 오름차순 정렬 및 합산 -> B 재배열 조건 고려 X
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

sorted_A = sorted(A, reverse=True)
sorted_B = sorted(B)

S = 0
for i in range(N):
    S += sorted_A[i] * sorted_B[i]

print(S)

######################################################
## A2. list A, B 내 최소 및 최대 추출하여 곱하고 이후 pop, 반복진행
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

S = 0
for i in range(N):
    S += min(A) * max(B)
    A.pop(A.index(min(A))) 
    B.pop(B.index(max(B)))

print(S)