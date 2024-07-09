# --------Dictionary---------{}
# it is used to store data values in {key:value} pairs
# They are unordered, mutable & don't allow duplicate keys
'''info = {
    "name": "last name",
    "jiya": "singh",
    "ayu": "shrivastavvv",
    "course": ["neet", "cricket"]
}
info["name"] = "your name here please"  # to change the key value
info["ayu"] = 7  # overwrite

info["fav color"] = "blue"  # to add NEW value in dict
print(info)
#print(info["ayu"])  # to print particular key value.
# =====methods in dict====
# myDict.keys() print all keys
print(info.keys())
print(len(info))
print(list(info.keys()))  # typcasting into list
#return value
print(info.values())
#return item
print(info.items())
#another way
pair = list(info.items())
print(pair[1])
#get method
print(info.get("ayu"))

#update method
new_dict = {"name" : "pratigya"}
info.update(new_dict)
print(info)'''


# -----Nested dictionary-------
# creating dictionary ke and-ar dictionary= not working
# student = {
#     "name" : "khushi"
#     "sub" : {
#     "phy": 99,
#     "chem" : 77,
#     "math" : 44
# }
# }
# print(student)



#==============Sets=========
# set is collection of unordered items.(no index)
# each element in the set must be unique & u=immutable.
# coll = {1, 2, 2, 3, "hello", "w", "w", 0, 5}
# print(coll)
# print(len(coll))

#createe empty set
'''call = set()
call.add(56)
call.add(8)
call.add(78)
call.add(2)
call.add(20000)

#call.remove(2)
#call.clear()
print(len(call))
call.pop()
print(call)'''

#union & intersection
set1 = {1, 2, 3, 4}
set2 = {1, 5, 8, 4}

print(set1.union(set2))
print(set1.intersection(set2))
