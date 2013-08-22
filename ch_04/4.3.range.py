# range(n)
print range(10)

# range(n, m)
print range(2,10)

# range(0,10,3)
print range(0, 10, 3)
print range(-10, -100, -30)

# combine range() and len()
a = ['Vincent', 'Had', 'a', 'little', 'bunny']
for i in range(len(a)):
    print i, a[i]
