# Data Tipleri
# Text Type
x = "Men Ibrahimov Hesret "
print(x)
print(type(x))

# Numeratic Type (int)
y = 18
print(y)
print(type(y))

# Numeratic Type (float)
z = 1.8
print(z)
print(type(z))

#Complex
a = 18j
print(a)
print(type(a))

# Ardicilliqlar (list)
e = ["kivi","banan","erik"]
print(e)
print(type(e))

# Ardicilliqlar (tuple)
r = ["kivi","banan","erik"]
print(r)
print(type(r))

# # range
t = range(18)
print(t)
print(type(t))

# bool
d = True
print(d)
print(type(d))

# Global Deyisen
w = "Ibrahimov"
def myFunc():
    w = "Hesret"
    print("Menim adim " + w)
myFunc()
print("Menim adim " + w)

# Operatorlar (Riyazi Operatorlar)

n = 15
m = 3

print(n + m)
print(n - m)
print(n * m)
print(n / m)
print(n % m)
print(n ** m)
print(n // m)

# Operatorlar (Teyinat Operatorlar)
f = 5
print(f)
f += 5
print(f)
f -= 5
print(f)
f *= 5
print(f)
f /= 5
print(f)
f %= 2
print(f)
f //= 5
print(f)
f **= 5
print(f)

# Operatorlar (Muqayise Operatorlar)
u = 68
i = 45
print(u == i)
print(u != i)
print(u > i)
print(u < i)
print(u <= i)
print(u >= i)

# Operatorlar (Mentiqi Operatorlar)
s = 17
print(s > 15 and s < 18)
print(s > 6 or s > 220)
print(not(s > 6 or s > 220))

# Sert Operatoru (if else)
g = 73
h = 34
if g > h:
  print("g boyukdur h-dan")
elif g == h:
  print("g ve h beraberdir")
else:
  print("g kicikdir -dan")