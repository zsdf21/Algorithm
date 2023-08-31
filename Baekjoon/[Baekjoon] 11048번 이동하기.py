# 이동하기
"""
준규는 N×M 크기의 미로에 갇혀있다. 
미로는 1×1크기의 방으로 나누어져 있고, 각 방에는 사탕이 놓여져 있다. 
미로의 가장 왼쪽 윗 방은 (1, 1)이고, 가장 오른쪽 아랫 방은 (N, M)이다.
준규는 현재 (1, 1)에 있고, (N, M)으로 이동하려고 한다. 
준규가 (r, c)에 있으면, (r+1, c), (r, c+1), (r+1, c+1)로 이동할 수 있고, 
각 방을 방문할 때마다 방에 놓여져있는 사탕을 모두 가져갈 수 있다. 
또, 미로 밖으로 나갈 수는 없다.
준규가 (N, M)으로 이동할 때, 가져올 수 있는 사탕 개수의 최댓값을 구하시오.

# 입력
첫째 줄에 미로의 크기 N, M이 주어진다. (1 ≤ N, M ≤ 1,000)

둘째 줄부터 N개 줄에는 총 M개의 숫자가 주어지며, 
r번째 줄의 c번째 수는 (r, c)에 놓여져 있는 사탕의 개수이다. 
사탕의 개수는 0보다 크거나 같고, 100보다 작거나 같다.


# 출력
첫째 줄에 준규가 (N, M)으로 이동할 때, 가져올 수 있는 사탕 개수를 출력한다.
"""

import sys
N, M = map(int, sys.stdin.readline().split())


# ans1) -> Index Error, 초기 이동 방향에 맞게 패딩 처리 필요 
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        
        # 세 방향으로부터 누적 사탕 수의 최대 + 현 좌표 내 사탕 수 
        dp[i+1][j+1] = arr[i+1][j+1] + max(arr[i][j], arr[i][j+1], arr[i+1][j])
        
print(dp[N][M])


# ans2) 좌, 상단 패딩 처리
arr = [[0]*(M+1)] + [[0] + list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[0]*(M+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        
        # 세 방향으로부터 누적 사탕 수의 최대 + 현 좌표 내 사탕 수 
        dp[i][j] = arr[i][j] + max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
        
print(dp[N][M])