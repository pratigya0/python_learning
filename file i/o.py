# f = open("hey123","w")
# f = open("hey123","a")
# data = f.read()
# print(data)
#
# line1 = f.readline()
# print(line1)
#
# line2 = f.readline()
# print(line2)

# f.write("am i the only good person in the world")
# f.write("\nyoyoyoy")
# f.close()
# # print(type(data))


'''f = open("hey123","r+")
f.write("12ka4, 4 2 ka 1 \n")
print(f.read())
f.close()'''


#=============SYNTAX FORM========
'''with open("hey123", "r") as f:
    data = f.read()
    print(data)'''

# with open("hey123", "w") as f:
#     f.write("new data")

'''with open("hey123", "a+") as f:
    f.write("ayu fayuu ewww")
    print(f.read())
    f.write("ayu fayuu ewww")
    f.close()'''

#============DELETING A FILE===============
'''using the os module'''
'''Module(like a code library) is a file written by another programmer that 
    generally has a functions we can use.
    
    import os
    os.remove(filename)'''
# import os
# os.remove("hey123.txt")

#practice questions
'''with open("practice.txt", "w") as f:
    f.write("Hi everyone\nwe are learning file I\O\n")
    f.write("using java.\nlike programming in java.")
with open("practice.txt", "r") as f:
    data = f.read()
new_data = data.replace("java", "python")
print(new_data)

with open("practice.txt", "w") as f:
    f.write(new_data)'''

'''
def check_for_word():
     word = "learning"
     with open("practice.txt", "r") as f:
         data = f.read()
         if(data.find(word) != -1):
            print("found")
         else:
            print("no fnd")

check_for_word()'''

def check_for_line():
    word = "programming"
    data = True
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1
        else:
            print("-1")
check_for_line()

with open("practice.txt", "r") as f:
    data = f.read()
    print(data)

    num = ""
    for i in range(len(data)):
        if(data[i] == ","):
            print(int(num)) #delete text part from the paragraph.
            num = ""
        else:
            num += data[i]






























































