num_l = [1, 2, 10, 5, 3, 7]


res = []
s = map(lambda x: x**2, num_l)  # map函数的用途
for i in s:
    res.append(i)

print(res)  # [1, 4, 100, 25, 9, 49]
