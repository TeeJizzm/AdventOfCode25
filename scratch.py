BOT = 0
TOP = 100

start = 50

x = -301
y = -199

a = 12
b = -98
c = -1


def get(num):
    return (abs(num // 100)), (num % 100)


print(x, get(x))
print(y, get(y))
print(a, get(a))
print(b, get(b))
print(c, get(c))
