# ----------LIST----------Mutable-[] value can be change
'''list = [7, 8, 90, 45, 32]

print(type(list))
print(list.append(50)) #jodna
print(list.sort(reverse=True))
list.reverse()
list.insert(0, 2)
list.pop(1)
print(list)'''

# ----Tuples-----Immutable () value cant be change
tup = (3, 2, 1, 4, 1, 1, 1, 1)
# tup.pop(3)
print(tup)
print(tup.index(1))# return the first occurance of value
print(tup.count(1))
tup1 = (1,)  # tu consider it as tuple
print(tup1)
print(type(tup1))
