"""
range 倒序
1: reversed(range(10))
2: range(10, 0, -1)
"""

i = 0
j = 0

for i in range(11, 0, -1):
    print((" " * j) + ("*" * i))
    i += 1
    j += 1
