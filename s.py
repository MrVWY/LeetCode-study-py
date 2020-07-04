import collections

str1 = ['a', 'a', 'b', 'd']
m = collections.Counter(str1)
print(m)

str2 = ['你', '好', '你', '你']
m1 = collections.Counter(str2)
print(m1.items())

