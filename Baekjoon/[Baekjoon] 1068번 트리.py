# 트리
"""
# 문제
트리에서 리프 노드란, 자식의 개수가 0인 노드를 말한다.

트리가 주어졌을 때, 노드 하나를 지울 것이다. 그 때, 남은 트리에서 리프 노드의 개수를 구하는 프로그램을 작성하시오. 노드를 지우면 그 노드와 노드의 모든 자손이 트리에서 제거된다.

# 입력
첫째 줄에 트리의 노드의 개수 N이 주어진다. N은 50보다 작거나 같은 자연수이다. 둘째 줄에는 0번 노드부터 N-1번 노드까지, 각 노드의 부모가 주어진다. 만약 부모가 없다면 (루트) -1이 주어진다. 셋째 줄에는 지울 노드의 번호가 주어진다.

# 출력
첫째 줄에 입력으로 주어진 트리에서 입력으로 주어진 노드를 지웠을 때, 리프 노드의 개수를 출력한다.
"""
import sys
input = sys.stdin.readline

n = int(input())        # 전체 노드 개수
arr = list(map(int, input().split())) # 각 노드의 부모 노드
k = int(input())        # 지울 노드 번호
cnt = 0                 # 리프 노드 count

def DFS(K, arr):      # k = 지울 노드 / arr = 각 노드의 부모 노드 표기
    arr[K] = -2       # 삭제 의미 -2로 대체
    
    for i in range(len(arr)):   
        if K == arr[i]:       
            DFS(i, arr)         # 삭제한 인덱스를 부모로 갖는 노드 찾고 재귀

DFS(k, arr)
cnt = 0
for i in range(len(arr)):
    if arr[i] != -2 and i not in arr: # (-2는 삭제 노드) & (arr에 존재하는 것은 부모 노드)
        cnt += 1
        
print(cnt)