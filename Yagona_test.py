import unittest
from datetime import datetime
from TalabaShaxsClass import Shaxs, Talaba

class ShaxsTalabaTest(unittest.TestCase):
    def setUp(self):
        self.shaxs1 = Shaxs('Nasiba', 'Muxtorova', 'AA3101369', 1989)
        self.talaba1 = Talaba('Ali', 'Valiyev', 'BB2109876', 2000, 'T12345')

    def test_create_shaxs(self):
        self.assertIsNotNone(self.shaxs1.ism)
        self.assertIsNotNone(self.shaxs1.familiya)
        self.assertIsNotNone(self.shaxs1.passport)
        self.assertIsNotNone(self.shaxs1.tyil)

    def test_create_talaba(self):
        self.assertIsNotNone(self.talaba1.ism)
        self.assertIsNotNone(self.talaba1.familiya)
        self.assertIsNotNone(self.talaba1.passport)
        self.assertIsNotNone(self.talaba1.tyil)
        self.assertIsNotNone(self.talaba1.idraqam)
        self.assertEqual(self.talaba1.bosqich,1)

    def test_get_info_shaxs(self):
        shaxs1_info = "Nasiba Muxtorova. Passport: AA3101369, 1989-yilda tug`ilgan"
        self.assertEqual(shaxs1_info, self.shaxs1.get_info())

    def test_get_info_talaba(self):
        talaba1_info ="Ali Valiyev. 1-bosqich. ID raqami: T12345"
        self.assertEqual(talaba1_info, self.talaba1.get_info())

    def test_get_age_shaxs(self):
        current_year = datetime.now().year
        shaxs1_age = current_year - self.shaxs1.tyil
        self.assertEqual(shaxs1_age, self.shaxs1.get_age())

    def test_get_age_talaba(self):
        current_year = datetime.now().year
        talaba1_age = current_year - self.talaba1.tyil
        self.assertEqual(talaba1_age, self.talaba1.get_age())

    def test_is_instance(self):
        self.assertIsInstance(self.shaxs1, Shaxs)
        self.assertIsInstance(self.talaba1, Talaba)
        self.assertIsInstance(self.talaba1, Shaxs)



unittest.main()

























        
