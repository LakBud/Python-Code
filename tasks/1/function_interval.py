print()

def f(x):
    return x**3 - 2**x + x - 2

start = int(input("Start x: "))
slutt = int(input("Slutt x: "))

print()
for x in range(start, slutt+1):
    print(f"x: -- {x:^8.2f} -- | y: -- {f(x):^20.2f} -- ")

