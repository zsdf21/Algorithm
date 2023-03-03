# Q6. 가장 긴 팰린드롬 부분 문자열을 출력하라.
import time
start_time = time.time()
time.sleep(1)

# 동적 프로그래밍으로 해결 가능한 전형적인 문제 & 투 포인터로 해결 가능한 문제
### ver1.
def longest_palin(s):

    # 예외 처리: s가 한글자 or 전체가 펠린드롬일 경우
    if len(s) < 2 or s == s[::-1]:
        return s

    # 팬린드롬을 판별하고 투 포인터 기준 확장해나가는 함수
    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1: right]

    result = ''

    # 슬라이딩 윈도우를 우측으로 이동
    for i in range(len(s) -1):
        result = max(result, 
          expand(i, i + 1), # expand 함수에 투입, 2칸짜리 sliding
          expand(i, i + 2), # 3칸짜리 sliding
          key = len)
    
    return result

input_str= 'abbanbabab'
result = longest_palin(input_str)

end_time = time.time()
time_ = end_time - start_time

print("result:", result)
print(f'time: {time_:.3f}')

