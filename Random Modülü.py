import random

a = random.random()
print(a)

b = random.uniform(1,50)
print(b)
c = random.randint(1,50)
print(c)

d = random.randrange(1,50)
print(d)

sayilar = range(0,50)
e = random.choice(sayilar)
print("listeden rastgele: ",e)

f = random.sample(sayilar,3)
print(f)