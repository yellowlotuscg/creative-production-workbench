import unittest
from creative.core import Concept,approve
class Tests(unittest.TestCase):
 def test_approval_requires_metadata(self):
  with self.assertRaises(ValueError): approve(Concept("x","y",[]))
if __name__=="__main__": unittest.main()
