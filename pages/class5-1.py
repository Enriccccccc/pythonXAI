import random

rolls = int(input("你想要擲幾次骰子？： "))

results = []

for i in range(rolls):
    dice = random.randint(1, 6)
    results.append(dice)

print("\n🎲 擲骰子的結果如下：")
for i, r in enumerate(results, 1):
    print(f"第 {i} 次：{r}")
