"""
python 36-dars "FUNKSIYANI TEKSHIRISH" 
Nasiba Abdulloyevna
28.07.2024
"""
import unittest
from Fibonachchi import fibonachchi

class FibonachchiTest(unittest.TestCase):
    def test_fibonachchi(self):
        self.assertEqual(fibonachchi((1,1,2,3,5,8,13,21,34,55)), True)
        self.assertEqual(fibonachchi((1,2,3,4,5,6,7)), False)
       

unittest.main()
