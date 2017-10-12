from ApiV1 import *
from ApiProxy import *
import unittest

class TestCreateAccount(unittest.TestCase):
  def setUp(self):
    apiProxy = FakeApiProxy()
    self.api = Api(apiProxy)

  def test_is_success(self):
    result = self.api.createAccount('yoba', 'yobagroup', '1234qwer', comment = 'петух')
    self.assertEqual(result.result, "1")
  
  def test_huypizda_not_empty(self):
    result = self.api.createAccount('yoba', 'yobagroup', '1234qwer', comment = 'петух')
    self.assertIsNotNone(result.huyPizda)
    
if __name__ == '__main__':
    unittest.main(exit=False)
    k=input("\n Hurray, looks like all tests are passed! Press any key to exit... o/")

