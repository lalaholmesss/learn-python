def func(a, b) :
    print(a + b)

def cem(*ededler) : # Turns the nums into a list of nums with *
    c = 0
    for eded in ededler :
        c += eded
    return c

print(cem(5, 6, 7, 8))