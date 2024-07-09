# wap to input 2 floating point numbers & print their average.
'''a = float(input("enter first num:  "))
b = float(input("enter second num:  "))
avg = (a+b)/2
print(int(avg))'''

# wap to input 2 int no., a and b.print True if a is greater than or equal to b. if not print False.
'''a = int(input("enter first num: "))
b = int(input("enter second num: "))
if (a>=b):
    print("True")
else:
    print("False")
print(a>=b)'''

# wap to input user's first name & print its length. wap to find the occurence of '$" in a string.
'''first_name = input("write your first name :  ")
print(first_name)
print("Lenght of your name is : ", len(first_name))
print("the count of the provided variable is: ", first_name.count("y"))'''

# wap to check if a number entered by the user is odd or even.
'''num = int(input("Give a number: "))
rem= num % 2
if (rem == 0):
    print("it is an even number")
else:
    print("odd :(")'''


# wap to find gratest of 3 num entered by the user
# Function to find the greatest among three numbers
# def find_greatest(num1, num2, num3):
#     return max(num1, num2, num3)


# Taking input from the user
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
#
# if (a >= b and a >= c):
#     print("first no. is larget", a)
# elif (b >= c):
#     print("second no. is largest", b)
# else:
#     print("third is largest", c)

#wap to check multiple of 7 or not
# q = int(input("entre a no. here: "))
# w = q % 7
# if (w == 0):
#     print( "true")
# else:
#     print("nope")

#wap to ask user to enter names of their 3 favorite movies & store them in a list.
# movies = []
# mov1 = input("Enter your 1st favorite movies name:  ")
# movies.append(mov1)
# mov2 = input("Enter your 2nd favorite movies name:  ")
# movies.append(mov2)
# mov3 = input("Enter your 3rd favorite movies name:  ")
# movies.append(mov3)
# print(movies)

#wap to check if a list contains a palindrome(look same from both side= ex:-maam ) of elements.
'''lis1 = [1, 2, 1, 0]
copy_lis1 = lis1.copy()
copy_lis1.reverse()

if(copy_lis1 == lis1):
    print("this is true palindrome")
else:
    print("Not a palindrome")'''


#wap to count the number od students with the "A" grade in the following tuple.
#["C", "D", "A", "A", "B", "B", "A"]
# tup = ["C", "D", "A", "A", "B", "B", "A"]
# print(tup.count("A"))
# tup.sort()
# print(tup)

#Store following word meanings in a python dictionary table: "a piece of furniture", "list of facts & figures"
# cat: "a small animal"
dict = {
    "cat" : "a small animal",
    "table" : ["a piece of furniture", "list of facts & figures"]
}
print(dict)

#You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students.
#"python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"
set = {
"python", "java", "C++", "python", "javascript",
    "java", "python", "java", "C++", "c"
}
print(len(set))

#WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one.
# Use subject name as key & marks as value. { }
emp = {}
x = int (input("Enter phy marks:  "))
emp.update({"phy" : x})

x = int (input("Enter maths marks:  "))
emp.update({"maths" : x})

x = int (input("Enter chem marks:  "))
emp.update({"chem" : x})

print(emp)

#Figure out a way to store 9 & 9.0 as separate values in the set.
# (You can take help of built-in data types)
value = {9, "9.0"}
set = {
    ("int", 9),
    ("float", 9.0)
}
print(value)
print(set)