# 적록색약
"""
크기가 N×N인 그리드의 각 칸에 R(빨강), G(초록), B(파랑) 중 하나를 색칠한 그림이 있다. 그림은 몇 개의 구역으로 나뉘어져 있는데, 구역은 같은 색으로 이루어져 있다. 
또, 같은 색상이 상하좌우로 인접해 있는 경우에 두 글자는 같은 구역에 속한다.
적록색약이 아닌 사람이 봤을 때 구역의 수는 총 4개이다. (빨강 2, 파랑 1, 초록 1) 하지만, 적록색약인 사람은 구역을 3개 볼 수 있다. (빨강-초록 2, 파랑 1)
그림이 입력으로 주어졌을 때, 적록색약인 사람이 봤을 때와 아닌 사람이 봤을 때 구역의 수를 구하는 프로그램을 작성하시오.

# 입력
첫째 줄에 N이 주어진다. (1 ≤ N ≤ 100)
둘째 줄부터 N개 줄에는 그림이 주어진다.

# 출력
적록색약이 아닌 사람이 봤을 때의 구역의 개수와 적록색약인 사람이 봤을 때의 구역의 수를 공백으로 구분해 출력한다.

"""
import sys

## 만약 재귀를 사용해서 풀어야 하는 문제라면, 아래 코드를 상단에 쓰는 것은 선택이 아닌 필수
## -> 파이썬의 기본 재귀 깊이 제한은 1000으로 매우 얕은 편, 따라서 재귀로 문제를 풀 경우 드물지 않게 이 제한에 걸리게 되는데, 
##    문제는 코딩테스트 환경에서는 에러 메시지를 볼 수 없다는 것
sys.setrecursionlimit(1000000)

N = int(sys.stdin.readline()) # 행렬 크기 정의
matrix = [list(sys.stdin.readline()) for _ in range(N)] # 행렬 정보 입력
visit_list = [[0] * N for _ in range(N)] # 해당 원소 고려 여부 확인 위한 list 정의
normal_cnt = 0
b_cnt = 0 # for color blindness

# phase 1) 탐색 가능 방법 정의
d = [(0, 1), (0, -1), (1, 0), (-1, 0)] # 그래프 내 일치 색상 탐색 위한 전체 이동 방법(우좌상하)
## ex. (0, 1) 이동 -> 인덱싱 기준 우측 한칸 이동(x축으로 한칸 이동)

# phase 2) 탐색 실행 함수 정의
def dfs(x, y):
    visit_list[y][x] = True     # 주어진 x, y는 탐색 완료로 변경(인덱싱 기준!=행렬 좌표 기준, y가 먼저 나옴)
    color = matrix[y][x]        # 주어진 y, x의 색깔이 현 시점 탐색 색깔
    
    for dx, dy in d:            # 상하좌우 color 일치 여부 탐색
        X, Y = x + dx, y + dy
        if (0 <= X < N) and (0 <= Y < N): # 아직 방문하지 않았고 & color가 일치한다면 -> 방문으로 변경 및 재귀(단일 카운트에 묶이기 때문)
            if visit_list[Y][X] == False and matrix[Y][X] == color:
                dfs(X, Y) # 방문한 적 없으며 이전과 color가 일치하면 재귀 실행
                
        
# phase 3) 반복문 실행 및 cnt 확인
for y in range(N): # 모든 x, y 좌표 반복
    for x in range(N):
        if visit_list[y][x] == False:   # 해당 y, x좌표에 방문하지 않았다면
            dfs(x, y)                   # 상하좌우 동일 color 탐색 실시
            normal_cnt += 1             # 재귀 빠져나오면 cnt + 1


# phase 4) 색맹 조건따라 그래프 변형 및 cnt 확인
for y in range(N):
    for x in range(N):
        if matrix[y][x] == 'G': # G -> R
            matrix[y][x] = 'R'

visit_list = [[0] * N for _ in range(N)] # visit list 재정의 및 동일하게 탐색 진행
for y in range(N): 
    for x in range(N):
        if visit_list[y][x] == False:   
            dfs(x, y)                   
            b_cnt += 1
            
print(normal_cnt, b_cnt)