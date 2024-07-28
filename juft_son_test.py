"""
python 36-dars "FUNKSIYANI TEKSHIRISH" 
Nasiba Abdulloyevna
28.07.2024
"""
import unittest
from juft_son import get_juft_son

class JuftSonTest(unittest.TestCase):
    def test_juft_son(self):
        self.assertEqual(get_juft_son([13, 64, 97, 100]), [64, 100])
        self.assertEqual(get_juft_son([]), [])
        self.assertEqual(get_juft_son([1, 3, 5, 7]), [])

unittest.main()
