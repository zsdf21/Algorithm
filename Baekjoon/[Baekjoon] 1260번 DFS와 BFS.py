# 1260. DFS & BFS
"""
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 
더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

# 입력
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 
간선의 개수 M(1 ≤ M ≤ 10,000), 
탐색을 시작할 정점의 번호 V가 주어진다.

다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 
어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

# 출력
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. 
V부터 방문된 점을 순서대로 출력하면 된다.
"""
import sys
N, M, V = map(int, sys.stdin.readline().split())
# N, M, V = map(int, input().split())

adj = [[] for _ in range(N+1)] # 인접행렬 생성
for _ in range(M): # 각 경로 M개를 start, end로 구분하여 인접행렬 리스트에 저장
    s, e = map(int, input().split()) # start node, end note split 및 모든 루트 adj에 저장
    adj[s].append(e)
    adj[e].append(s) # 리스트 내 각 인덱스에 연결 생성, 양방향으로 해야하니 양쪽 모두 생성 
# print(adj)


# phase 1) 오름차순 정렬(작은 수를 가진 노드를 우선하여 가기 위함)
for i in range(1, N+1): # 0은 빈 요소
    adj[i].sort() # 오름차순 정렬

  
# phase 2) dfs 정의, 방문 리스트 채우기
## 재귀 구조 주의: def 안에 재귀에 활용되면 안되는 인자 투입 불가
def dfs(c):             # current(시작 노드)    
    ans_dfs.append(c)   # 방문 노드를 리스트에 추가
    v[c] = 1            # 방문 기록 표시
    
    for n in adj[c]:    # 방문한 노드에서 인접한 요인 순차 산출
        if not v[n]:    # 방문 기록이 없다면 (if v[n] == 0):
            dfs(n)      # 방문 후 재귀 진행


# phase 3) bfs 정의, 방문 리스트는 broad 방식으로(특정 q 기준 모두 돌고 이후 수행)
def bfs(s):    
    q = []              # 필요한 변수 q(방문 리스트), v(방문 기록) 생성  
    q.append(s)         # q에 초기 데이터(시작 노드) 삽입
    ans_bfs.append(s)   # 초기 데이터 삽입
    v[s] = 1            # visit 표시
    
    while q:
        c = q.pop(0)        # 너비 기반, 방문한 q에서 이미 append한 첫 인자 날리고
        for n in adj[c]:    # c에서 연결된 노드 하나씩 꺼내서 안가본 노드라면 q에 삽입
            if not v[n]:
                q.append(n)
                ans_bfs.append(n)
                v[n] = 1    # visit 방문으로 표시 
                
    # print(*ans_bfs)

# phase 4) 출력
v = [0]*(N+1)       # 방문기록
ans_dfs = []        # 방문 리스트 
## 위 두 변수는 재귀에 들어가면 안됨
dfs(V)

v = [0]*(N+1)       # 방문기록
ans_bfs = [] 
bfs(V)

print(*ans_dfs)
print(*ans_bfs)