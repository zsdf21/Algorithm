# 3273. 두 수의 합
"""
n개의 서로 다른 양의 정수 a1, a2, ..., an으로 이루어진 수열이 있다. 
ai의 값은 1보다 크거나 같고, 1000000보다 작거나 같은 자연수이다. 
자연수 x가 주어졌을 때, ai + aj = x (1 ≤ i < j ≤ n)을 만족하는 (ai, aj)쌍의 수를 구하는 프로그램을 작성하시오.

# 입력
첫째 줄에 수열의 크기 n이 주어진다. 다음 줄에는 수열에 포함되는 수가 주어진다. 셋째 줄에는 x가 주어진다. (1 ≤ n ≤ 100000, 1 ≤ x ≤ 2000000)


# 출력
문제의 조건을 만족하는 쌍의 개수를 출력한다.
"""
import sys

n = int(sys.stdin.readline())
num_array = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())

ans = 0

# ans1) 반복문 활용, 모든 경우의 수 탐색 -> time error
for i in range(n):
    for j in range(n - i):
        if num_array[i] + num_array[-j] == x:
            ans += 1

print(ans)

# ans2) 투 포인터 활용(탐색 시간 축소 위해), 정렬 후 각 포인터 기준 크기 비교 후 탐색 진행
num_array.sort()
left, right = 0, n-1

while left < right: 
    tmp = num_array[left] + num_array[right] # 크기 비교 위한 tmp 생성
    if tmp == x:
        ans += 1
        left += 1   # left가 연속 같은 수일 경우 고려 위해

    elif tmp < x:
        left += 1   # left 이동
    else: 
        right -= 1  # right 기준 같은 수일 경우 고려 위해
        
print(ans)

