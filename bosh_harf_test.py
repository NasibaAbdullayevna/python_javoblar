"""
python 36-dars "FUNKSIYANI TEKSHIRISH" 
Nasiba Abdulloyevna
28.07.2024
"""
import unittest
from bosh_harf import get_text_title
class TitleTest(unittest.TestCase):
    def test_title(self):
        self.assertEqual(get_text_title(['men yurtimni sevaman','men maqsadimga yetaman']),['Men Yurtimni Sevaman','Men Maqsadimga Yetaman'])
                
unittest.main()
