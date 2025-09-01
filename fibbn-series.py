a=1
b=1
print(a)
print(b)
counter = 0
while counter < 4:
    a = a + b
    b = a + b
    print(a)
    print(b)
    counter = counter + 1
