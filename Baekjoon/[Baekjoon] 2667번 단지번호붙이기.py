# 단지번호붙이기
"""
<그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 
철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 
여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 
대각선상에 집이 있는 경우는 연결된 것이 아니다. 
<그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 지도를 입력하여 단지수를 출력하고, 
각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.


# 입력
첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 
그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.


# 출력
첫 번째 줄에는 총 단지수를 출력하시오. 
그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.
"""
import sys
sys.setrecursionlimit(10**6)

# ans1) BFS
## 방문하지 않은 집 1을 만나면 -> 큰 유닛을 찾기 위해 루프 돌도록 작성

N = int(sys.stdin.readline()) # 행렬 크기 정의
# matrix = [list(sys.stdin.readline()) for _ in range(N)] # 행렬 정보 입력 -> 본 문제에서 Error 유발
matrix = [list(map(int, input())) for _ in range(N)]

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # 이동 가능 네 방향 
visited = [[0]*N for _ in range(N)]     # 특정 집 방문 여부 확인 위한 방문 리스트
unit = [] # ans                         # 각 단지들의 집 개수를 담을 유닛 리스트

def find_unit(x, y):   
    q = []              # 1-2-3단계 집 등 breadth 탐색 위한 q 리스트
    q.append((x, y))    # 해당 단계에 해당하는 집 넣고
    visited[x][y] = 1   # 해당 집 방문 표시
    count = 1           # 유닛 내 집 개수 카운팅
    
    while q:                # q에 값이 존재함 -> 탐색 진행해야 함. 
        cx, cy = q.pop(0)   # q의 첫 값을 뽑아서 네방향으로 집 유무 탐색
        
        for dx, dy in d:
            X, Y = cx + dx, cy + dy
            
            # 4방향 이동 + 조건-범위내 & 미방문 + 집이 있으면 -> 다음 단계 루프 돌기위해 q에 삽입 
            if (0<=X<N) and (0<=Y<N) and (visited[X][Y] == 0) and (matrix[X][Y] == 1): # boolean 연산에는 and사용(&는 integer 기반 연산에 사용)
                q.append((X, Y))    # 다음 단계 위해 q에 삽입 
                visited[X][Y] = 1   # 방문 체크
                count += 1          # 해당 유닛에 집 있으니 카운트 +1
    return count                    # 갈수 있는 집 다 돌면 -> count return


for i in range(N):
    for j in range(N):
        # 전체 순회하며 발견하지 않은 지역 발견시 fint_unit 탐색
        if (matrix[i][j] == 1) & (visited[i][j] == 0):
            unit.append(find_unit(i, j))
            
unit.sort()
print(len(unit), *unit, sep='\n')


######################################################
# ans2) DFS, 약간은 다른 스타일 풀이
## BFS와 DFS 시간효율성은 비슷한 수준

N = int(input())
matrix = [list(map(int, input())) for _ in range(N)]
unit = []
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # 이동 가능 네 방향 

def DFS(x,y):
    if x<0 or x>=N or y<0 or y >=N:     # 범위를 벗어날 경우 -> False
        return False
    
    if matrix[x][y] == 1:               # 만약 집이 있다면
        global count
        count += 1                      # 해당 집 count
        matrix[x][y] = 0                # 유닛 내 집으로 counting 이후 0으로 수정(중복 막기 위해) -> visited 행렬과 같은 역할
        for dx, dy in d:                # 네 방향 탐색하고
            X, Y = x + dx, y + dy
            DFS(X,Y)                    # 각 방향별 DFS 재귀 수행
        return True                     # 만약 집이 있다면 True 반환
    return False                        # 집이 없을 경우(모두 0 -> False)
    
count = 0
result = 0

for i in range(N):
    for j in range(N): 
        if DFS(i,j) == True:
            unit.append(count)
            result += 1
            count = 0
        
unit.sort()
print(len(unit), *unit, sep='\n')
