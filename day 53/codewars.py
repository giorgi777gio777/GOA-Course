# 1)
def repeat_str(repeat, string):
    return repeat * string

# 2)
def remove_char(s):
    return s[1:-1]

# 3)
def square_sum(numbers):
    sum = 0
    for num in numbers:
        square = num * num
        sum = sum + square
    return sum 

# 4)
def find_smallest_int(arr):
    small = arr[0]
    for num in arr:
        if small > num:
            small = num
    return small  