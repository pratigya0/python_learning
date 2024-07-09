#string & condition statement
#
# str1 = "This is a dtring.\ni am otring"
# print(str1)
#
# #indexing
# str = "Apna_college"
# print(str[0])

#str doesnot support item assingment.

#slicing- accessing parts of a string
#str[starting_idx : ending_inx] ending endex is not included

str = "pratiyogita"
print(str[2:5])

#str.endswith("er") #return true if string ends with substr.
pop = "hello i am in banaras"
print(pop.endswith("ras"))

#str.captalize
pip = "hello i am in banaras"
#pip = pip.capitalize()  it will keep cap the sentence all the time we print it.
print(pip.capitalize())

#str.replace(old, new)
sip = "hello i \n am in banaras"
print(sip.replace("hello", "Hiii"))

#str.find
lol = "hello i lo am in banaras"
print(lol.find("m"))

#str.count("am")
pol = "hello i lo am in am am am am banaras"
print(pol.count(" am"))