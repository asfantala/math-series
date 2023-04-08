
def fibonacci(n):
    """
  n : An integer representing Fibonacci number .
   if n=1 it will return 1 
   and if n= 0 it will return 0 
   else it will return the nth Fibonacci number
    """
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def lucas(n):

    '''
      n : An integer representing lucas number .
   if n=1 it will return 1 
   and if n= 0 it will return 2 
   else it will return the nth lucas number
    
    '''
    if n == 1:
        return 1

    elif n == 0:
        return 2
    else:
        return lucas(n-1) + lucas(n-2)


def sum_series(n, first=0, second=1):
    """
Computes and returns the nth number in a series that starts with the given first and second numbers.
If the first and second arguments are not provided, the function defaults to the Fibonacci series.
 first (int): The first number in the series. Defaults to 0.
 second (int): The second number in the series. Defaults to 1
    """
    if n == 0:
        return first
    elif n == 1:
        return second
    else:
        return sum_series(n-1, first, second) + sum_series(n-2, first, second)
