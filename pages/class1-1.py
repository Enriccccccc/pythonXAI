# 這是單行註解
"""
這是多行註解
"""

nl = 3  # 這是整數
f1 = 3.14  # 這是浮點數
b1 = True  # 這是布林值
s1 = "hello"  # 這是字串

print(3)
print(3.14)
print(True)
print("hello")
a = 10
b = 20
c = a + b
print(a + b)  # 加法
print(a - b)  # 減法
print(a * b)  # 乘法
print(a / b)  # 除法
print(a // b)  # 整除
print(a % b)  # 取餘數
print(a**b)  # 次方

print("hello + world")  # word connect
print("hello" + " " + "world")  # word connect
print("hello" * 3)  # word repeat
print("hello" + "world" * 3)  # word connect and repeat

name = "Enric"
age = "67"
new_str = f"my name is {name} , and I am {age} years old."  # f-string
print(new_str)
print(len(""))  # 0
print(len("hi"))  # 2
print(len("hello"))  # 5
print(type(10))
print(type(3.14))
print(type("hello"))
print(type(True))
print(int(True))  # 1
print(int(False))  # 0
print(int(1234))  # 1234

print(float(3.14))  # 3.14
print(float(10))  # 10.0

print(bool(1))  # True
print(bool(0))  # False
print(bool(-2))  # True
print(bool(""))  # False
print(bool("hello"))  # True

print(str(1234))  # "1234"
print(str(3.14))  # "3.14"
print(str(True))  # "True"
print(str(False))  # "False"

in1 = input("請輸入內容：")
print("你輸入的內容是：" + in1)
print(type(in1))  # str

# in1 = int(input("請輸入整數："))
# print("你輸入的整數是：" + (in1))
# print(type(in1))  #str

r = int(input("請輸入半徑："))
area = 3.14 * r**2
print(f"半徑為 {r} 的圓面積是 {area}")
