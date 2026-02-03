L1 = []
print({})  # empty list

L2 = [1, 2, 3, 4, 5]
print(L2)  # number list

L3 = ["apple", "banana", "cherry"]
print(L3)  # number list

L4 = [1, "apple", True, 3.14]
print(L4)  # mixed list

L5 = [1, 2, 3, [4, 5]]
print(L5)  # nested list

# get the element of the list
print(L5[1])  # 2
print(L5[3])  # [4,5]
print(L5[3][0])  # 4

L6 = [1, 2, 3, "a", "b", "c"]
L7 = L6[::2]
print(L7)  # [1,2,"b"]
L8 = L6[1:4]
print(L8)  # [2,3,"a"]
L9 = L6[1:4:2]
print(L9)  # [2,"a"]
