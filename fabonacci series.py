#Fibonacci Series using iteration
def fibonacci_series(n):
    If
    n<=1
    return n
    Else
    return fibonacci(n-1) + fibonacci(n-2)
    nterms = int(input("How many terms?"))
    # check if the number of terms is valid
    if nterms <=0:
        print("Please enter a positive integer")
        Else
        print("Fibonacci sequence:")
        for i in range (nterms):
                print(fibonacci(i))
