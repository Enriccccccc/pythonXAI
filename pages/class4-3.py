# easy fuction
def hello():
    print("hello")


hello()
hello()
hello()


# function with parameters
def greet(name):
    print(f"hello {name}")


print("-" * 30)
greet("Enric")
greet("Yuson")


# 帶回船值得函數
def two_num_min(a, b):
    if a < b:
        return a
    else:
        return b


print(two_num_min(3, 5))
print(two_num_min(10, 7))


def three_num_min(a, b, c):
    if a < b:
        if a < c:
            return a
        else:
            return c
    else:
        if b < c:
            return b
        else:
            return c


print("-" * 30)

print(three_num_min(1, 5, 2))  # 1
print(three_num_min(10, 7, 15))  # 7
print(three_num_min(8, 12, 6))  # 6


def calculate_circle_area(radius, pi=3.14):
    return pi * radius**2


print(calculate_circle_area(10))  # 314.0
print(calculate_circle_area(10, 3.14159265358979323846))  # 314.1592653589793

print("-" * 30)


def print_parameters(a, b, c=0, d=0):
    print(f"a:{a}, b:{b}, c:{c}, d:{d}")


print_parameters(1, 2)  # a:1, b:2, c:0, d:0
print_parameters(1, 2, 3)  # a:1, b:2, c:3, d:0
print_parameters(1, 2, 3, 4)  # a:1, b:2, c:3, d:4
print_parameters(1, 2, d=4)  # a:1,b:2,c:0,d:4
