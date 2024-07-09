'''
name = input("what is your name? ")

print("Hello " + name)  # concatenation
# superhero name & shw it on terminal
superhero = input("what is your superhero name? ")
print(superhero)

# type_conversion(all the input in python come in int from
old_age = input("enter your old age: ")
new_age = int(old_age) + 2
print("your new age is " + str(new_age))'''

'''# methods in str
name = "Pratigya Singh"
print(name.index('S'))
print(name.find('i'))
print(name.upper())
print(name.replace("Pratigya Singh", "khushi"))  # it_cn_replace_char_too
print(name)

# keyword(they are highlighted by purple)
# here_we_are_finding_existing_substance
print('r' in name)'''

# arithmetic_operators
'''print(5 // 2)  # removes the decimal part from the output
print(4 ** 2)  # power operator

# shotcuts
i = 9
# i = i + 9
i += 9  # called as shot-cut
print(i)
# operator precedence
o = ((9 + 6) * 9)
print(o)

# comparision operator
7<8
8>4
5==8
5!=8
print(2>3 or 7>1) #or operator

#AND = it print true if both condition is ture otherwise false will be printed
print (3>6 and 9< 8)

#NOT operator convert true to false, false to T
print(not 2>3)'''

# if and else statement
'''age = 8
if age >= 78:
     print("yolo")

elif age < 5:
    print("yor r in scl")
else:
    print("you r cute") '''

# calculator
'''first = input("your first no :  ")
op = input("select the operator(+,-,*,/,%): ")
second = input("your second no : ")
first = int(first)
second = int(second)
if op == "+" :
    print(first + second)
elif op == "-" :
    print(first - second)
elif op == "*" :
    print(first * second)
elif op == "/" :
    print(first / second)
elif op == "%" :
    print(first % second)
else:
    print("Invalid input")'''

# loops
'''i=1
while i <= 6:
    print(i * "*")
    i = i + 1

i = 9
while i >= 0:
    print(i * "*")
    i = i- 1

for i in range(4):
    print(i + 1)'''

# lists
marks = [786, 5, 5]
'''print(marks[0:2])
print(marks [-1]) #[] shows index position, -1 starts counting from behind

marks.append(8)
marks.insert(0,63) #to add in starting
print(5 in marks)
print("length os marks =   " + str(len(marks)))
print(marks)

i = 0
while i < len(marks):
    print(marks[i])
    i = i + 1
marks.clear()
print(marks)'''

# break & continue
students = ["ram", "ri", "uo", "lo", "raju"]

'''for student in students:
    if student == "raju":
        break;
    print(student)

for student in students:
    if student == "uo":
        continue;
    print(student)'''

'''# tuples
marks = (96, 56, 23, 23, 23, 23)
print(marks.count(23))
print(marks.index(96))

# sets(we can find index valur directly)
marks = {96, 56, 23, 23, 23}
print(marks)

for score in marks:
    print(score)

# Dictionary (key, value) store together
marks = {"english": 95, "chem": 96}
print(marks["chem"])
marks["physics"] = 55;  # adding new subject
print(marks)'''

# FUNCTIONS (in-built fun, module fun, user-defined fun)
'''import math
print(dir(math))

from math import *
print(sqrt(16))
print(radians(8))

#def fun_name(parameters)
def print_sum(first, second):
    print(first + second)

print_sum(1, 5)'''

#if we multiply numerical value with str
'''A, B = -12, 5
Txt = '@'
print(12*Txt*5)
c = A//B
print(c)'''

#conditional statements {single line if/ternary operator}
#<var>=<var1>if<condition>else<val2>
'''name = input("name :  ")
nik = "yes" if name == "pratigya" else "none"
print (nik)

#<stt1>if<condition>else<stt2>
food = input("food : ")
print("good job") if food == "cake" or food == "cherry" else print("bad")'''

#clever if/Ternary operator
#<var> = (false_val, true_val)[<condition>]
'''age = int(input("age : "))
vote = ("yes", "no")[age <= 18]
print(vote)'''

# sal = float(input("salary :  "))
# tax = sal*(0.1, 0.2) [sal >= 50000]
# print(tax)

#assingment operators
# num = 102
# p = 78
# o = 8
# l = 7
# k = 2
# u = 56
# num += 5 # += oprator
# p -= 4
# o *= 5
# l /= 7
# k %= 2
# u **= 2
# print(num, p, o, l, k, u)

#relation operator (==, !=, <, >, <=, >=)

#Logical operator (not, and, or)
'''a = 50
b = 30
# print(not False)
# print(not True)
print(not(a>b))
print(not(a<b))

val1 = True
val2 = False
print("ans operator: ", val1 and val2) #t&t=true'''
#print("ans operator: ", val1 or val2)#forf=false
#print("ans operator: ", a == b or a > b)

#Type conversion
a, b = 1, 2.0
sum = a+b
print(int(sum))