import random
for i in range(30):
    i1=random.randint(5,14)
    a=str(i1).zfill(2)
    i2=random.randint(0,59)
    i2=str(i2).zfill(2)
    a=a+":"+i2
    print(a)
print()
print()
for i in range(30):
    i1=random.randint(15,22)
    a=str(i1).zfill(2)
    i2=random.randint(0,59)
    i2=str(i2).zfill(2)
    a=a+":"+i2
    print(a)


