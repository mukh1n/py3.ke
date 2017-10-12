from metapi import *
from apiProxy import *
import unittest

class TestCreateAccount(unittest.TestCase):
  def setUp(self):
    proxy = FakeApiProxy()
    self.client = ApiClient(proxy)

  def test_is_success(self):
    result = self.client.createAccount('yoba', 'yobagroup', '1234qwer', comment = 'петух')
    self.assertEqual(result.result, "1")
  
  def test_huypizda_not_empty(self):
    result = self.client.createAccount('yoba', 'yobagroup', '1234qwer', comment = 'петух')
    self.assertIsNotNone(result.huyPizda)
    
if __name__ == '__main__':
    unittest.main(exit=False)
    k=input("\n Hurray, looks like all tests are passed! Press any key to exit... o/")
