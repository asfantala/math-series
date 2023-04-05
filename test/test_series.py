import pytest
from series import fibonacci
from series import lucas
from series import sum_series
"""
fibonacci

n==0 = 0
n==1 = 1

"""

def test_one():
 actual= fibonacci(0)
 excepted = 0
 assert actual == excepted

def test_two():
  actual= fibonacci(1)
  excepted = 1
  assert actual == excepted

def test_three():
  actual= fibonacci(2)
  excepted = 1
  assert actual == excepted

def test_four():
  actual= fibonacci(3)
  excepted = 2
  assert actual == excepted    

def test_five():
  actual= fibonacci(4)
  excepted = 3
  assert actual == excepted 

def test_six():
  actual= fibonacci(5)
  excepted = 5
  assert actual == excepted   

def test_seven():
  actual= fibonacci(6)
  excepted = 8
  assert actual == excepted   


  """
  lucas
    n == 0: 2
    n == 1: 1
  """

def test_lucas0():
  actual= lucas(0)
  excepted = 2
  assert actual == excepted

def test_lucas1():
  actual= lucas(1)
  excepted = 1
  assert actual == excepted  

def test_lucas2():
  actual= lucas(2)
  excepted = 3
  assert actual == excepted 

def test_lucas3():
  actual= lucas(3)
  excepted = 4
  assert actual == excepted 

def test_lucas4():
  actual= lucas(4)
  excepted = 7
  assert actual == excepted 


"""
sum series
"""  
def test_sumseries0():
  actual= sum_series(0)
  excepted = 0
  assert actual == excepted 

def test_sumseries1():
  actual= sum_series(1)
  excepted = 1
  assert actual == excepted  

def test_sumseries2():
  actual= sum_series(2)
  excepted = 1
  assert actual == excepted

def test_sumseries3():
  actual= sum_series(3)
  excepted = 2
  assert actual == excepted 

def test_sumseries4():
  actual= sum_series(4)
  excepted = 3
  assert actual == excepted 


def test_sumseries5():
  actual= sum_series(0,2,1)
  excepted = 2
  assert actual == excepted 

def test_sumseries6():
  actual= sum_series(1,2,1)
  excepted = 1
  assert actual == excepted 

def test_sumseries7():
  actual= sum_series(2,2,1)
  excepted = 3
  assert actual == excepted   

def test_sumseries8():
  actual= sum_series(3,2,1)
  excepted = 4
  assert actual == excepted 