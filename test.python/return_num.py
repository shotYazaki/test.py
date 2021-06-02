a = 0
n = 0
while a < 12:#逆数の和が12を
    n += 1#整数を a < 12 となるまで順番に足して行く
    a += 1 / n #逆数の和
print(n-1)
print(a - 1/(n))
print(n)
print(a)