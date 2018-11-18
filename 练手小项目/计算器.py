import re

def string_fliter(str_nums):
    str_nums = str_nums.replace(' ', '')
    str_nums = str_nums.replace('+-', '-')
    str_nums = str_nums.replace('--', '+')
    return str_nums


def bracket_out(inner_nums):
    inner_nums = inner_nums.replace('(', '')
    inner_nums = inner_nums.replace(')', '')
    return inner_nums


def calculate(nums):
    list_nums = list(nums)
    return_sum_num = 0
    print(list_nums)
    while True:
        if '*' in list_nums:
            return_sum_num = list_nums.pop(0)
            for i in list_nums:
                if i != '*':
                    return_sum_num *= int(i) 
            list_nums.clear()
        elif '+' in list_nums:
            if '+' in list_nums[0]:
                del list_nums[0]
            if '-'
            for i in list_nums:
                if i != '+':
                    return_sum_num += int(i)
            list_nums.clear()
        elif '-' in list_nums:
            if '-' in list_nums[0]:
                del list_nums[0]
                return_sum_num -= int(list_nums.pop(0))
            for i in list_nums:
                if i != '-':
                    return_sum_num -= int(i)
                    
        else:    
            return str(return_sum_num)
        

def main(str_nums):
    str_nums = string_fliter(str_nums)
    sum_num = 0
    while True:
        # 匹配两边是括号的中间不是括号的,最内层的括号
        inner_nums = re.search('\([^()]+\)', str_nums)
        if inner_nums:
            # 交给函数把左右括号去除,返回一个字符串
            bracket_out_after = bracket_out(inner_nums.group())
            # 将去除括号的字符串进行计算,返回计算好的字符串
            result = calculate(bracket_out_after)
            # 将返回回来的数字替换到最内层括号
            str_nums = re.sub('\([^()]+\)', result, str_nums, 1)    
        else:
            sum_num += int(calculate(str_nums))
            print(sum_num)
            break
        
        


if __name__ == '__main__':
    str_nums = input('>>>>>')
    main(str_nums)


