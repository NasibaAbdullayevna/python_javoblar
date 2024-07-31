import unittest
from datetime import datetime
from TalabaShaxsClass import Shaxs

class Shaxs_test(unittest.TestCase):
    
    def setUp(self):
        ism='Nasiba'
        familiya='Muxtorova'
        passport='AA3101369'
        self.tyil=1989
        self.shaxs1=Shaxs(ism,familiya,passport,tyil=self.tyil)

    def test_creat(self):
        self.assertIsNotNone(self.shaxs1.ism)
        self.assertIsNotNone(self.shaxs1.familiya)
        self.assertIsNotNone(self.shaxs1.passport)
        self.assertIsNotNone(self.shaxs1.tyil)

    def test_get_info(self):
        shaxs1_info="Nasiba Muxtorova. Passport: AA3101369, 1989-yilda tug`ilgan"
        self.assertEqual(shaxs1_info,self.shaxs1.get_info())

    def test_get_age(self):
        shaxs1_age=datetime.now().year-self.tyil
        self.assertEqual(shaxs1_age,self.shaxs1.get_age())

    

    
unittest.main()
