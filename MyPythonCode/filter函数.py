# movie_people = ['zyh', 'wpq', 'sb_alex', 'sb_yh']
# movie_people = ['zyh', 'wpq', 'alex_sb', 'yh_sb']
#
#
# def sb_show(name):
#     return name.endswith("sb")
#
#
# def filter_test(func, array):
#     res = []
#     for p in array:
#         if not func(p):
#             res.append(p)
#     return res
#
#
# print(filter_test(sb_show, movie_people))  # ['zyh', 'wpq']
#
#
# # 终极版本
# def filter_test(func, array):
#     res = []
#     for p in array:
#         if not func(p):
#             res.append(p)
#     return res
#
#
# print(filter_test(lambda name: name.endswith('sb'),
#                   movie_people))  # ['zyh', 'wpq']


# filter函数
# movie_people = ['zyh', 'wpq', 'alex_sb', 'yh_sb']
# res = list(filter(lambda name: not name.endswith('sb'),
#                   movie_people, ))
# print(res)
