a = 15
for i in range(2, a//2 + 1):
    if a % i == 0:
        print("Not prime")
        break
else:
    print("Prime")
