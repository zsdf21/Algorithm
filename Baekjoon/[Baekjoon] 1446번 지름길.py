# 지름길
"""
# 문제
매일 아침, 세준이는 학교에 가기 위해서 차를 타고 D킬로미터 길이의 고속도로를 지난다. 
이 고속도로는 심각하게 커브가 많아서 정말 운전하기도 힘들다. 
어느 날, 세준이는 이 고속도로에 지름길이 존재한다는 것을 알게 되었다. 
모든 지름길은 일방통행이고, 고속도로를 역주행할 수는 없다.

세준이가 운전해야 하는 거리의 최솟값을 출력하시오.

# 입력
첫째 줄에 지름길의 개수 N과 고속도로의 길이 D가 주어진다. 
N은 12 이하인 양의 정수이고, D는 10,000보다 작거나 같은 자연수이다. 
다음 N개의 줄에 지름길의 시작 위치, 도착 위치, 지름길의 길이가 주어진다. 
모든 위치와 길이는 10,000보다 작거나 같은 음이 아닌 정수이다. 
지름길의 시작 위치는 도착 위치보다 작다.

# 출력
세준이가 운전해야하는 거리의 최솟값을 출력하시오.
"""

import sys
N, D = map(int, sys.stdin.readline().split())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

min_dis = [i for i in range(D+1)] # ex. [0-150]

# ans1) i에서의 최단 거리를 지속적으로 업데이트, 최종 D까지 최단거리를 도출
for i in range(D+1): # 매 거리 시점에서 최단거리 측정
    if i > 0:
        min_dis[i] = min(min_dis[i], min_dis[i-1] + 1)          # i까지 거리의 최단거리는 min_dis or 직전거리 + 1 ex) min_dix = [1, 2, 3, 4, 5...150]
        
    for s, e, d in arr:                                         # 지름길 반영하여 min_dis update
        # 조건) 시작 지점이 s / e가 전체길이 이하 / e번째까지 도달 길이보다 i번째 길이 + d 가 작아야(지름길이 더 작아야 함)
        if i == s and e <= D and min_dis[i] + d < min_dis[e]:   # s값이 i번째 시작, e가 D보다 작고
            min_dis[e] = min_dis[i] + d                         # e 번째 mis_dis의 값 초기화(지름길로 가는 걸로 설정)

print(min_dis[D])
