# global variable and local variable
length = 5


def calculate_square_area1():
    area = length**2  # local variable
    print("area is", area)


calculate_square_area1()

length = 10  # local variable

print("-" * 30)


def calculate_square_area2():
    area = length**2  # local variable
    print("area is", area)


calculate_square_area2()

print("-" * 30)

# length = 5


# def calculate_square_area3():
#     area = length**2  # local variable


# length = 10  # global variable
# calculate_square_area3()
# print("area is", area)

print("-" * 30)

length = 5  # local variable
area = 3.14 * 10**2  # global variable


def calculate_square_area4():
    area = length**2


calculate_square_area4()
print("area is", area)

print("-" * 30)

print("-" * 30)

# length = 5  # local variable
# area = 3.14 * 10**2  # global variable


# def calculate_square_area5():
#     print("area is", area)
#     area = length**2
#     print("area is", area)


# calculate_square_area5()

print("-" * 30)

length = 5  # local variable
area = 3.14 * 10**2  # global variable


def calculate_square_area6():
    area = length**2
    return area


area = calculate_square_area6()
print("area is", area)


print("-" * 30)

length = 5  # local variable
area = 3.14 * 10**2  # global variable


def calculate_square_area7():
    global area
    area = length**2


area = calculate_square_area6()
print("area is", area)
