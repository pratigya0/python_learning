#============FUNCTIONS IN PYTHON & RECURSION================
'''Block of statements that perform a specific task.   
def func_name(parameters1, param2....):
#some work
return val

func_name(arg1, arg2..)'''# function call

#function def
'''def cal_sum(a, b):#parameters
    sum = a+b #function call; arguments
    print(sum)
    return sum
cal_sum(5, 6)
cal_sum(500, 6)

def cal_sum(b, m):
    return b + m
s = cal_sum(2, 3)
print(s)

#print avg of 3 numbers>
def avg_num(a, b, c):
    avg = a+b+c/3
    print(avg)
    return avg
avg_num(2, 2, 2)

print("khushi", end=" ")
print("singh")

#wap to print the len of the list (list is parameteres).
integers = [1,2]
o = ["ok", "no", "77"]
def know_len(list):
    print(len(list))
    return list
know_len(integers)
know_len(o)

#wap to print the element of the list in single line.(list is the parameter)
o = ["ok", "no", "77" ]
print(o[0], end=" ")
print(o[1], end=" ")
print(o[2])

def print_list(list):
    for item in list:
        print(item, end=" ")

print_list(o)'''

#waf to find the factorial of n.
'''def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)
cal_fact(5)'''

#waf to convert usd to inr
# def converter(usd_val):
#     inr_val = usd_val * 83
#     print(usd_val, "USD = ", inr_val, "INR")
#     return inr_val
# converter(2)


'''when a function call it self repeatedly'''
# def show(n):
#     if (n == 0): #base case
#         return
#     print(n)
#     show(n-1)
#     print("END")
# show(8)


#factorial in recursion
'''def fact(n):
    if(n==1  or n==0):
        return 1
    else:
        return fact(n-1) * n
print(fact(4))'''

# write a recursive function to calc the sum of first n natural numbers.
'''def num(n):
    if (n == 0):
        return 0
    return num(n-1) + n
print(num(5))'''


#print all the element of list.

def print_list(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)

pop = ["pip", "pops", "yup", "ilu", "tup"]

print_list(pop)
























