# 算術指定運算子

a = 10
b = 3
a += b  # equals to a=a+b
print("a+=b_result")

a = 10
b = 3
a -= b  # equals to a=a-b
print("a-=b_result:", a)

a = 10
b = 3
a *= b  # equals to a=a*b
print("a*=b_result:", a)

a = 10
b = 3
a /= b  # equals to a=a/b
print("a/=b_result:", a)

a = 10
b = 3
a //= b  # equals to a=a//b
print("a//=b_result:", a)

a = 10
b = 3
a %= b  # equals to a=a%b
print("a%=b_result:", a)

a = 10
b = 3
a **= b  # equals to a=a**b
print("a**=b_result:", a)


print("-" * 30)

# while loop practice
i = 0
while i < 5:
    print("i =", i)
    i += 1

print("-" * 30)

# while loop break
i = 1
while 1 < 6:
    if i == 3:
        break
    print("i =", i)
    i += 1

# for loop break

print("-" * 30)

for i in range(1, 6):
    if i == 3:
        break
    print("i =", i)
