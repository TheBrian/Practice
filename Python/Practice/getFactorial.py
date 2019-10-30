def getFactorial(n):
    "factorial recursion"
    if n < 2:
        return 1
    else:
        return n * getFactorial(n-1)

n = getFactorial(10)

print(n)