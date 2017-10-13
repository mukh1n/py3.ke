import unittest
import random 

DEFAULT_PASSWORD = '123qwe'

class BaseTest(unittest.TestCase):

  @property
  def randomHex(self):
    return '%030x' % random.randrange(16**30);