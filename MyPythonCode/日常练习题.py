# 给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。
# 你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。
# 示例:
# 给定 nums = [2, 7, 11, 15], target = 9
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
# 做题思路:
# 因为要数组的下标,所以使用数组的长度进行遍历
# 一层遍历从0到len(array), 
# 二层遍历从0+1到len(array),
# 为了让两个循环的下标不是统一的
# 判断,如果array[x] + array[y] == num
# 则返回
# def two_sum(array, num):
#     result = []
#     for x in range(0, len(array)):
#         for y in range(x+1, len(array)):
#             if array[x] + array[y] == num:
#                 return [x, y]
# array = [3, 2, 4]
# num = 6
# for i in two_sum(array, num):
#     print("1---->", i)


# 给定一个 32 位有符号整数，将整数中的数字进行反转。 
def reverse_num(num):
    reverse_num = list(str(num))
    if num < 0:
        reverse_num[1:] = reverse_num[:0:-1]
        return int("".join(reverse_num))
    else:
        reverse_num = reverse_num[::-1]
        if reverse_num[0] == "0":
            reverse_num.remove(reverse_num[0])
        return int("".join(reverse_num)) 
print(reverse_num(-18))
print(reverse_num(18))
print(reverse_num(180))

    



