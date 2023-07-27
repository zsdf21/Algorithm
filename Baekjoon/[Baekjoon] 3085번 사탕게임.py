# 사탕 게임
'''
가장 처음에 N×N크기에 사탕을 채워 놓는다. 
사탕의 색은 모두 같지 않을 수도 있다. 상근이는 사탕의 색이 다른 인접한 두 칸을 고른다. 
그 다음 고른 칸에 들어있는 사탕을 서로 교환한다. 
이제, 모두 같은 색으로 이루어져 있는 가장 긴 연속 부분(행 또는 열)을 고른 다음 그 사탕을 모두 먹는다.

사탕이 채워진 상태가 주어졌을 때, 상근이가 먹을 수 있는 사탕의 최대 개수를 구하는 프로그램을 작성하시오.
'''

'''
입력
첫째 줄에 보드의 크기 N이 주어진다. (3 ≤ N ≤ 50)
다음 N개 줄에는 보드에 채워져 있는 사탕의 색상이 주어진다. 빨간색은 C, 파란색은 P, 초록색은 Z, 노란색은 Y로 주어진다.
사탕의 색이 다른 인접한 두 칸이 존재하는 입력만 주어진다.

출력
첫째 줄에 상근이가 먹을 수 있는 사탕의 최대 개수를 출력한다
'''

# A1. counting / 인접 변환 파트 구별하여 구현
N = int(input())
matrix = [list(input()) for _ in range(N)]
ans = 0

## counting 함수
def counting(matrix):
    max_cnt = 1 # 최소 1개에서 시작
    
    for i in range(N):
        cnt = 1
        for j in range(0, N-1): # 각 열에서 최대치 탐색(연속된 색의 사탕 개수 cnt+1)
            if matrix[i][j] == matrix[i][j+1]: cnt += 1
            else: cnt = 1
            max_cnt = max(max_cnt, cnt)

        cnt = 1
        for j in range(0, N-1): # 각 행에서 최대치 탐색
            if matrix[j][i] == matrix[j+1][i]: cnt += 1
            else: cnt = 1
            max_cnt = max(max_cnt, cnt)
    
    return max_cnt

## 인접 변환 및 max count 계산
for i in range(N): # 모든 행 다 돌고
    for j in range(N): # 모든 열 다 돌고
        
        # 특정 행과 특정 열 기준에서 변환
        if j < N-1: # j와 j+1 변환, 범위 설정
            # 인접한 사탕끼리 변환 -> 열 기준
            matrix[i][j], matrix[i][j+1] = matrix[i][j+1], matrix[i][j] # 행 고정 & 열 바꿔준 이후
            cnt = counting(matrix)  # max count
            ans = max(ans, cnt)     # 계산된 값 업데이트
            # 다음 열 반복 재탐색 위한 원위치
            matrix[i][j], matrix[i][j+1] = matrix[i][j+1], matrix[i][j]

        if i < N-1: # 행 범위(i, i+1 변환 위해)
            matrix[i][j], matrix[i+1][j] = matrix[i+1][j], matrix[i][j] # 열 고정 & 행 바꿔준 이후
            cnt = counting(matrix)  # max count
            ans = max(ans, cnt)     # 계산된 값 업데이트
            # 다음 행 반복 재탐색 위한 원위치
            matrix[i][j], matrix[i+1][j] = matrix[i+1][j], matrix[i][j]

print(ans)