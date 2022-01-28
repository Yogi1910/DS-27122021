
print('module is being imported..ta da....imported!')

def table(number):
    for i in range(11):
        print("{} * {} = {}".format(number,i,number*i))
        
        
def factorial(n):
    if n<=1:
        return 1
    else:
        n=n*factorial(n-1)
        return n
        
        
date = 28