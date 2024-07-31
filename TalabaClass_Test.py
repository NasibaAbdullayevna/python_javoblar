import unittest
from datetime import datetime
from TalabaShaxsClass import Talaba

class Talaba_test(unittest.TestCase):
    
    def setUp(self):
        ism='Nasiba'
        familiya='Muxtorova'
        passport='AA3101369'
        self.idraqam='N0000001'
        self.bosqich=1
        self.tyil=1989
        self.talaba1=Talaba(ism,familiya,passport,idraqam=self.idraqam,tyil=self.tyil)

    def test_creat(self):
        self.assertIsNotNone(self.talaba1.ism)
        self.assertIsNotNone(self.talaba1.familiya)
        self.assertIsNotNone(self.talaba1.passport)
        self.assertIsNotNone(self.talaba1.idraqam)
        self.assertIsNotNone(self.talaba1.bosqich)
        self.assertIsNotNone(self.talaba1.tyil)

    def test_get_id(self):
        talaba1_id=self.idraqam
        self.assertEqual(talaba1_id,self.talaba1.get_id())

    def test_get_bosqich(self):
        talaba1_bosqich=self.bosqich
        self.assertEqual(talaba1_bosqich,self.talaba1.get_bosqich())

    def test_get_info(self):
        talaba1_get_info="Nasiba Muxtorova. 1-bosqich. ID raqami: N0000001"
        self.assertEqual(talaba1_get_info,self.talaba1.get_info())
        
    
unittest.main()
