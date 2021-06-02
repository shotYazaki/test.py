
total = 0
num = 1000000000
for i in range(1, num+1):
    if num % i == 0:
        if i <= 100000:
            print(i)