# 수고르기
"""
N개의 정수로 이루어진 수열 A[1], A[2], …, A[N]이 있다. 
이 수열에서 두 수를 골랐을 때(같은 수일 수도 있다), 
그 차이가 M 이상이면서 제일 작은 경우를 구하는 프로그램을 작성하시오.

예를 들어 수열이 {1, 2, 3, 4, 5}라고 하자. 
만약 M = 3일 경우, 1 4, 1 5, 2 5를 골랐을 때 그 차이가 M 이상이 된다. 
이 중에서 차이가 가장 작은 경우는 1 4나 2 5를 골랐을 때의 3이 된다.

# 입력
첫째 줄에 두 정수 N, M이 주어진다. 다음 N개의 줄에는 차례로 A[1], A[2], …, A[N]이 주어진다.


# 출력
첫째 줄에 M 이상이면서 가장 작은 차이를 출력한다. 항상 차이가 M이상인 두 수를 고를 수 있다.
"""

import sys
N, M = map(int, sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(N)]
# A1) Two Pointer
arr.sort()                  # 계산 경우의 수 줄이기 위해 정렬
l, r = 0, 0
ans = float("inf")

while l < N and r < N:
    if arr[r] - arr[l] < M:
        r += 1
    else:
        ans = min(ans, arr[r] - arr[l])
        l += 1

print(ans)

# A2) 함수 스타일
arr.sort()                  # 계산 경우의 수 줄이기 위해 정렬

def solution(arr, N, M):    
    ans = float("inf")
    l, r = 0, 0             

    while r < N:                # 조건) r이 전체 크기보다 작아야 함
        diff = arr[r] - arr[l]  # 현 시점 diff

        if diff < M:            # 현 시점 diff가 M보다 작으면 -> r만 우측 이동(diff 크게 하기 위해)
            r += 1              

        elif diff > M:          # 조건 충족 -> l 시점 최소 차 구했으니 ans 저장 및 다음 값 탐색(l 우측 이동) 
            ans = min(diff, ans)
            l += 1
        else:
            return M
    return ans

ans = solution(arr, N, M)
print(ans)