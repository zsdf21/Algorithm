# 알파벳

"""
## 1. sys limit 너무 크게하면 -> 메모리 초과 error 유발 가능
sys.setrecursionlimit는 메모리를 우선적으로 잡는 개념, 
sys.setrecursionlimit(10 ** 6)을 하니 메모리 초과

## 2. 재귀의 경우 
python3 : 메모리 및 속도 측에서 우세; pypy3: 복잡한 코드(반복)을 사용하는 경우 우세
+) set 내 영문을 받고 제거하는 과정에서 시간 초과 유발 가능
"""

"""
세로 R칸, 가로 C칸으로 된 표 모양의 보드가 있다. 
보드의 각 칸에는 대문자 알파벳이 하나씩 적혀 있고, 좌측 상단 칸 (1행 1열) 에는 말이 놓여 있다.
말은 상하좌우로 인접한 네 칸 중의 한 칸으로 이동할 수 있는데, 
새로 이동한 칸에 적혀 있는 알파벳은 지금까지 지나온 모든 칸에 적혀 있는 알파벳과는 달라야 한다. 
즉, 같은 알파벳이 적힌 칸을 두 번 지날 수 없다.
좌측 상단에서 시작해서, 말이 최대한 몇 칸을 지날 수 있는지를 구하는 프로그램을 작성하시오. 
말이 지나는 칸은 좌측 상단의 칸도 포함된다.

# 입력
첫째 줄에 R과 C가 빈칸을 사이에 두고 주어진다. (1 ≤ R,C ≤ 20) 
둘째 줄부터 R개의 줄에 걸쳐서 보드에 적혀 있는 C개의 대문자 알파벳들이 빈칸 없이 주어진다.


# 출력
첫째 줄에 말이 지날 수 있는 최대의 칸 수를 출력한다.
"""
# Ans 1) Set 경로 지정, time error
import sys
sys.setrecursionlimit(10**5)
R, C = map(int, sys.stdin.readline().split(' ')) # 행렬 크기 정의

matrix = [(sys.stdin.readline()) for _ in range(R)] # 행렬 정보 입력

d = [(0, 1), (0, -1), (1, 0), (-1, 0)] # 행렬 내 이동 방향(우좌상하)

alphas = set() # -> 영문을 받고 제거하는 과정에서 시간 초과 유발
ans = 1

def dfs(x, y, cnt):
    global ans
    ans = max(cnt, ans)
    
    for dx, dy in d:            # 상하좌우 color 일치 여부 탐색
        X, Y = x + dx, y + dy    
        
        if 0 <= X < C and 0 <= Y < R and not matrix[Y][X] in alphas: # 미방문일 경우
            alphas.add(matrix[Y][X])
            dfs(X, Y, cnt+1)
            alphas.remove(matrix[Y][X]) # 특정 for문에 해당하는 재귀에서 빠져나온 이후 해당 노드는 제거해야 함.

alphas.add(matrix[0][0]) 
dfs(0, 0, 1)
print(ans)


# Ans 2) 방문 여부 효율적 확인
## 아스키코드 변환 ord() -> ex. ord(matrix[0][0])
R, C = map(int, input().split())
matrix = list(input() for _ in range(R))

ans = 1
alphas = [0]*128

def dfs(x, y, cnt):
    global ans
    ans = max(ans, cnt)

    # 4방향, 범위내, 중복값이 아닌경우
    for dx,dy in ((-1,0),(1,0),(0,-1),(0,1)):
        X, Y = x + dx, y + dy
        if 0<= X < R and 0 <= Y < C and alphas[ord(matrix[X][Y])] == 0:
            alphas[ord(matrix[X][Y])] = 1
            dfs(X, Y, cnt+1)
            alphas[ord(matrix[X][Y])] = 0

alphas[ord(matrix[0][0])] = 1 # 해당 값을 사용했음(방문표시)
dfs(0, 0, 1)
print(ans)

# Error 확인 필요
# import sys
# sys.setrecursionlimit(10**5)

# def dfs(x, y, cnt):
#     global ans
#     ans = max(cnt, ans)
    
#     for dx, dy in d:            # 상하좌우 color 일치 여부 탐색, 4방향 / 범위 내 / 중복값 아닌 경우
#         X, Y = x + dx, y + dy    
       
#         if 0 <= X < C and 0 <= Y < R and not alphas[ord(matrix[Y][X])]==0: # 범위 먼저 체크(out of index 주의) + 미방문일 경우
#             alphas[ord(matrix[Y][X])]=1
#             dfs(X, Y, cnt+1)
#             alphas[ord(matrix[Y][X])]=0 # 특정 for문에 해당하는 재귀에서 빠져나온 이후 해당 노드는 제거해야 함.


# R, C = map(int, sys.stdin.readline().split(' ')) # 행렬 크기 정의
# matrix = [(sys.stdin.readline()) for _ in range(R)] # 행렬 정보 입력

# alphas = [0]*128 # 문자열까지의 아스키코드 개수 128개 
# ans = 1
# d = [(0, 1), (0, -1), (1, 0), (-1, 0)] # 행렬 내 이동 방향(우좌상하)

# alphas[ord(matrix[0][0])] = 1 # 초기 값 방문
# dfs(0, 0, 1)
# print(ans)