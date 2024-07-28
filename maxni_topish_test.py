"""
python 36-dars "FUNKSIYANI TEKSHIRISH" 
Nasiba Abdulloyevna
28.07.2024
"""
import unittest
from maxni_topish import get_max
class MaxTest(unittest.TestCase):
    def test_max(self):
        self.assertEqual(get_max(3,5,5),5)
        self.assertEqual(get_max(7,7,1),7)
        self.assertEqual(get_max(12,7,3),12)
        self.assertEqual(get_max(1,19,23),23)
        self.assertEqual(get_max(0,0,0),0)

unittest.main()
