def factorial(x):

    if x==0 or x==1:
      return 1
    else:
       return x * factorial(x-1)
    
x=int(input("Enter number:"))
print(factorial(x))
print(factorial(x).__doc__)