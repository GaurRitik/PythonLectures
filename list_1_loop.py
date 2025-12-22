nums=[10,22,31,54,15]
x=55
index=0
for val in nums:
    if val==x:
        print("Found at index:",index)
        break
    index += 1
else:
    print("Not found")
# The else block executes only if the loop is not terminated by a break statement