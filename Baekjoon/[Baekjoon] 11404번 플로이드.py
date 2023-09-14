# 플로이드
"""
# 문제
n(2 ≤ n ≤ 100)개의 도시가 있다. 
그리고 한 도시에서 출발하여 다른 도시에 도착하는 m(1 ≤ m ≤ 100,000)개의 버스가 있다. 
각 버스는 한 번 사용할 때 필요한 비용이 있다.

모든 도시의 쌍 (A, B)에 대해서 도시 A에서 B로 가는데 
필요한 비용의 최솟값을 구하는 프로그램을 작성하시오.

# 입력
첫째 줄에 도시의 개수 n이 주어지고 둘째 줄에는 버스의 개수 m이 주어진다. 
그리고 셋째 줄부터 m+2줄까지 다음과 같은 버스의 정보가 주어진다. 
먼저 처음에는 그 버스의 출발 도시의 번호가 주어진다. 
버스의 정보는 버스의 시작 도시 a, 도착 도시 b, 한 번 타는데 필요한 비용 c로 이루어져 있다. 
시작 도시와 도착 도시가 같은 경우는 없다. 비용은 100,000보다 작거나 같은 자연수이다.
시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있다.

# 출력
n개의 줄을 출력해야 한다. 
i번째 줄에 출력하는 j번째 숫자는 도시 i에서 j로 가는데 필요한 최소 비용이다. 
만약, i에서 j로 갈 수 없는 경우에는 그 자리에 0을 출력한다.
"""

import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())     

INF = float('inf')

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
cost = [[INF] * n for _ in range(n)]

########### ans1) ###########
## 1. 이동 필요없는 동일 도시 0 출력
for i in range(n):
    for j in range(n):
        if i == j:
            cost[i][j] = 0

## 2. graph에 담긴 직접 가는 경우의 수 고려
for i, j, c in graph:
    cost[i-1][j-1] = min(c, cost[i-1][j-1]) # 인덱스 0시작 고려, -1

## 3. j -> k 에서 i를 경우하는 경우 고려
for i in range(n):          # i는 경유지
    for j in range(n):      # j는 출발지
        for k in range(n):  # k는 도착지
            cost[j][k] = min(cost[j][k], cost[j][i] + cost[i][k])

## 4. INF인 도착하지 못하는 경로 0으로 수정
for i in range(n):
    for j in range(n):
        if cost[i][j] == INF:
            cost[i][j] = 0
            
# 출력 주의
for i in range(0, n):
    for j in range(0, n):
        print(cost[i][j], end=' ')
    print() # j까지 돌고 다음 줄 띄움 @@아오

# print(cost)            
# for i in range(n):
#     print(cost[i])


########### ans2) Error -> 몇 경우의 수 고려 X ###########

# for i, j, c in graph: 
#     # 직접 가는 경우의 수
#     cost[i-1][j-1] = min(cost[i-1][j-1], c) 

#     # m을 경유하는 경우 고려( + 직접 가는 것보다 경유하여 가는 것이 더 짧은 것 또한 고려)
#     for i2, m, c2 in graph:          
#         if i == i2:                     # 경유지를 따질 때 출발점이 같을 때만 고려
#             for i3, m2, c3 in graph:    # 경유지에서 도착지가 존재할 때 고려
#                 if (i3 == m) and (j == m2):
#                     cost[i-1][j-1] = min(cost[i-1][j-1], c2+c3)
               
               
# for i in range(m):
#     for j in range(m):
#         if cost[i][j] == INF:
#             cost[i][j] = 0               

# print(cost)
