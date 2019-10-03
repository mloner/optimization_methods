import unittest
import math

from passive_search import passive_search

def func_1(x):
    return 4*x**3 - 8*x**2 - 11*x + 5

arr_of_func = [func_1]

class TestSingleVariableOptimization(unittest.TestCase):

    def test_passive_search(self):
        
        for func in arr_of_func:
            min_index = passive_search(-1, 2, 10, func)
            min_value = func(min_index)

            print(f"x={min_index} y={min_value}")
        
if __name__ == '__main__':
    unittest.main()
        
