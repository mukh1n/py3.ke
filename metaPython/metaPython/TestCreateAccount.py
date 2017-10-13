import unittest
import metatesting
from metatesting import *
from metapi import *
from apiProxy import *

class TestCreateAccount(metatesting.BaseTest):
  def setUp(self):
    proxy = FakeApiProxy()
    self.client = ApiClient(proxy)

  def test_is_success(self):
    #given
    group = self.client.createGroup('yobagroup' + self.randomHex)
    #when
    result = self.client.createAccount('yoba' + self.randomHex, group.name, DEFAULT_PASSWORD, comment = 'петух')
    #then
    self.assertEqual(result.result, "1")
  
  def test_huypizda_not_empty(self):
    #given
    group = self.client.createGroup('yobagroup' + self.randomHex)
    #when
    result = self.client.createAccount('yoba' + self.randomHex, group.name, DEFAULT_PASSWORD, comment = 'петух')
    #then
    self.assertEqual(result.result, "1")
    self.assertIsNotNone(result.huyPizda)
    

if __name__ == '__main__':
    unittest.main(exit=False)
    k=input("\n Hurray, looks like all tests are passed! Press any key to exit... o/")

