import random

target = random.randint(0, 100)

min_val = 0
max_val = 100
while True:
    num = int(input(f"請輸入一個{min_val}到{max_val}的數字："))
    if num < min_val or num > max_val:
        print("wut are u doin")
    elif num < target:
        print("biigger")
        min_val = num + 1
    elif num > target:
        print("smaller")
        max_val = num - 1
    else:
        print("goody boi, u did it")
        break
