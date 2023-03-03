# Q14. 정렬되어 있는 두 연결 리스트를 합쳐라
import typing
import collections
from collections import deque
import time

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

start_time = time.time()
time.sleep(1)

root = start = ListNode(None)
root.next = head



# palin(input_str)
end_time = time.time()
time_ = end_time - start_time

print(f'time: {time_:.3f}')