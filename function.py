def sum (a, b):
    sum=a+b
    return sum
print(sum(3,4))

# can't(same variable and func name) be in the same namespace
sum = 3
print(sum)
print(sum(10,20))