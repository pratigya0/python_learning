# #=========Loops in python======
# #loops are used to repeat instruction.
#
# #while loops: #some work
#
# count = 1
# while count<=10:
#     print("hey")
#     count += 1
#
# # print numbers from 5 to 1
# o = 5
# while o >= 1:
#     print(o)
#     o -= 1
#
# i = 1
# while i <= 100:
#     print(i)
#     i += 1
#
# i = 100
# while i >= 1:
#     print(i)
#     i -= 1

# multiplication n
# n = int(input("Enter your number:  "))
# i = 1
# while i <= 10:
#     print(n*i)
#     i += 1

# print the list using loop
#list = []

'''i = 1
while i<=100:
    print(i)
    i += 3'''

#Wap in python Print the elements of the following list using a loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
'''num = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
index = 0
while index < len(num):
    print(num[index])
    index += 1

# searching for a no. in tuple using loop\
tup = (1, 4, 16, 25, 26, 45, 25, 64, 81, 100)

find = 25
i = 0 #initialization
while i < len(tup):
    if (tup[i] == find):
        print("found at indx", i)
    else:
        print("finding babe.....")
    i += 1'''

#==========Break $ continue=======

'''p = 1
while p <= 9:
    if(p == 7):
        p += 1
        continue #skip
    print(p)
    p += 1
'''

#===========FOR LOOP==========
'''num = [1, 2, 3, 4, 5]

for val in num:
    print(val)

str = "PRATIGYA $$ SINGH"

for val in str:
    print(val)'''

#QUES1
#num = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

# for el in num:
#     print(el)

'''x = 81
idx = 0
for el in num:
    if (el == x):
        print(" num found", idx)
        break
    idx += 1'''

######====RANGE()=========#######
'''range functions returns a sequence of numbers, starting from 0 by default, and increments by 1(by default),
 and stops before a specified number.'''
# seq = range(5)
# for i in seq:
#     print(i)
#
# for i in range(2, 20, 3):
#     print(i)

#print no from 100 to 1.
'''row_values = []
for i in range(100, 0, -1):
    row_values.append(i)

print(row_values)

#multiplication of n number.
n = int(input("Enetr the num:   "))
for i in range(1, 11):
    print(n*i)'''

#=============PLACE STATEMENT=========
'''pass is a null statement that does nothing. its used as a placeholder for future code'''
# for i in range(9):
#     pass
# print("hellooo")

#wap to find the sum of first n natural numbers.(using while)
'''n = 5
sum = 0
# for i in range(n+1):
#     sum += i
i = 1
while i <= n:
    sum += i
    i += 1
print("total sum: ", sum)'''

#wap to find factorial of first n numbers.(using for loop)
n = 5
fact = 1
i = 1
for i in range(i, n+1):
    fact *= i
print("factorial = ", fact)
# while i <= n:
#     fact *= i
#     i += 1
# print("factorial = ", fact)



