nums = [1,4,7,10,13]
total = 0
for x in nums:
    if x % 2 == 0:
        total = x + total
print (total)