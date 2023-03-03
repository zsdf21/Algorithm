# Q2. 문자열을 뒤집는 함수를 작성하라
# 입력값은 문자배열, 리턴없이 리스트 내부를 직접 조작하라. 
import time
input_str = ["h", "e", "l", "l", "o"]
start_time = time.time()
time.sleep(1)

##################### ver1. #####################

def reverse_str(s):
    s.reverse()

for _ in range(9):
    reverse_str(input_str)

##################### ver2. #####################

# def reverse_str(s):
#     left, right = 0, len(s)-1

#     while left < right:
#         s[left], s[right] = s[right], s[left]
#         left += 1
#         right -= 1

# for _ in range(9):
#     reverse_str(input_str)

##################### ver3. 슬라이싱의 경우 return이 있어야 None값이 출력되지 않는 한계가 존재함. 

# def reverse_str(s):
#     return s[::-1]

# for _ in range(9):
#     input_str = reverse_str(input_str)

##################### ver4. 문자열일 경우? #####################

# def reverse_str(s):
#      result = ""
#      idx = len(s) - 1
#      while idx >= 0:
#          result += s[idx]
#          idx -= 1
#      return result

# for _ in range(9):
#     input_str = reverse_str(input_str)

##################### ver5. 문자열일 경우? #####################

# def reverse_str(s):
#   return ''.join(reversed(s))

# for _ in range(9):
#     input_str = reverse_str(input_str)

##########################################

end_time = time.time()
time_ = end_time - start_time

print("result:", input_str)
print(f'time: {time_:.3f}')