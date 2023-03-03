# Q7. 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라
import time
start_time = time.time()
time.sleep(1.0)

num_list = [2, 9, 11, 5, 8, 13, 12, 32, 1]
target_num = 7

# 리트코드 1번 문제로 최적화 가능한 여러 수단이 존재하는 문제임. 

########## ver1.########## 브루트 포스 방식(무차별 대입 방식), 시간 복잡도: O(n2)
def twosum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

########## ver2.########## in을 이용한 탐색, 시간 복잡도는 위와 동일하나 연산이 훨씬 빠르고 가벼운 특징-in. 
# def twosum(nums, target):
#     for i, n in enumerate(nums):
#         complement = target - n

#         if complement in nums[i+1:]:
#             return [nums.index(n), nums[i+1:].index(complement) + (i + 1)]

########## ver3.########## 첫 수를 뺀 결과 키 조회
def twosum(nums, target):
    nums_map = {}

    # 키, 값을 바꿔서 딕셔너리 저장
    for i, num in enumerate(nums):
        nums_map[num] = i

    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            return [i, nums_map[target - num]]


# ########## ver4.##########
def twosum(nums, target):
    nums_map = {}

    # ver3.의 풀이에서 하나의 for 문으로 통합
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target - num], i]
        nums_map[num] = i

########## 오답 ##########
def twosum(nums, target):
    left, right = 0, len(nums) - 1
    while not left == right:
        # 합이 타겟보다 작으면 왼쪽 포인터를 오른쪽으로
        if nums[left] + nums[right] < target:
            left += 1

        # 합이 타겟보다 크면 오른쪽 포인터를 왼쪽으로
        elif nums[left] + nums[right] > target:
            right -= 1

        else: 
            return [left, right]

            
result = twosum(num_list, target_num)

end_time = time.time()
time_ = end_time - start_time

print("result:", result)
print(f'time: {time_:.3f}')

