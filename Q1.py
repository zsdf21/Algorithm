strs = 'abbca'

def palindrome(s):
    s = s.lower()
    return s==s[::-1]

print(palindrome(strs))

# s: pd.DataFrame) -> pd.Series
# assert type(s) == pd.DataFrame():
# error code 반환

# isinstance(s, pd.Series):
# s = pd.DataFrame()
# else:
#     TypeError


from collections import defaultdict
a = defaultdict(list) # int
b= dict()
# collections.defaultdict
# 체크할 때 최초 값 있냐 없냐 체크할 때 list 나오냐 안나오냐 가능 try accept하면 한번 루프 도는 것이라서 비효율. 
