def  factorial(n):
    if  n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
m = int(input("please enter a number: "))
print(factorial(m))