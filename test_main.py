import unittest
import main

class TestMain(unittest.TestCase):
  def test_accept_criteria(self):
    result = main.testScoreRank()
    self.assertEqual(result, "Accept")

  def test_reject_criteria(self):
    result = main.testScoreRank()
    self.assertEqual(result, "Reject")
  
if __name__ == "__main__":
  unittest.main()