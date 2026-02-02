print(1 == 1)  # True
print(1 != 1)  # False
print(2 > 1)  # True
print(2 < 1)  # False
print(2 >= 1)  # True
print(2 <= 1)  # False

print(not True)  # False
print(not False)  # True

print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False

print(True or True)  # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False

password = input("請輸入密碼：")
if password == "1234":
    print("welcome Enric")

if password == "1234":
    print("welcome Enric")
else:
    print("密碼錯誤，請重新輸入")
if password == "1234":
    print("welcome Enric")
elif password == "5678":
    print("welcome Yuson")
else:
    print("密碼錯誤，請重新輸入")
