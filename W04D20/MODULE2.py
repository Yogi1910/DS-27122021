def factorial(n):
    if n<=1:
        return 1
    else:
        n=n*factorial(n-1)
        return n