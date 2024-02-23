
def euk(a,b):
    while b:
        a, b = b, a % b
    return a
print(euk(12,18))