###############################################################################
#   Class:          INFT1207
#   Authors:        Robert Macklem
#   Date:           January 31 2024
#   File:           ICE3_unittest.py
#   Description:    Unit testing file for ICE2_Updated.py in the app package of
#                   the project directory.
###############################################################################
import unittest
from ICE3.app.ICE2_Updated import MinimumFinder


# Unit testing class
class TestMinimumFinder(unittest.TestCase):
    def testCase1(self):
        mini = MinimumFinder()
        self.assertEqual(90, mini.find_minimum([90]))  # 1A
        self.assertEqual(10, mini.find_minimum([12, 10]))  # 1B
        self.assertEqual(10, mini.find_minimum([10, 12]))  # 1C
        self.assertEqual(12, mini.find_minimum([12, 14, 36]))  # 1D
        self.assertEqual(12, mini.find_minimum([36, 14, 12]))  # 1E
        self.assertEqual(12, mini.find_minimum([14, 12, 36]))  # 1F

    def testCase2(self):
        mini = MinimumFinder()
        self.assertRaises(TypeError, mini.find_minimum([]))

    def testCase3(self):
        mini = MinimumFinder()
        self.assertEqual(10, mini.find_minimum([10, 23, 34, 81, 97]))  # 3A
        self.assertEqual(10, mini.find_minimum([97, 81, 34, 23, 10]))  # 3A

    def testCase4(self):
        mini = MinimumFinder()
        self.assertEqual(-2, mini.find_minimum([10, -2, 5, 23]))
        self.assertEqual(-24, mini.find_minimum([10, -2, -24, 4]))

    def testCase5(self):
        mini = MinimumFinder()
        self.assertEqual(-56, mini.find_minimum([-23, -31, -45, -56]))  # 5A
        self.assertEqual(-203, mini.find_minimum([-6, -203, -2, -78]))  # 5B

    def testCase6(self):
        mini = MinimumFinder()
        self.assertRaises(TypeError, mini.find_minimum([23, 34.56, 67, 33]))

    def testCase7(self):
        mini = MinimumFinder()
        self.assertRaises(TypeError, mini.find_minimum([23, "hi", 32, 1]))  # 7A
        self.assertRaises(TypeError, mini.find_minimum([12, "&", "*", "34m", "!"]))  # 7B

    def testCase8(self):
        mini = MinimumFinder()
        self.assertEqual(3, mini.find_minimum([3, 4, 6, 9, 6]))  # 8A
        self.assertEqual(6, mini.find_minimum([13, 6, 6, 9, 15]))  # 8B

    def testCase9(self):
        mini = MinimumFinder()
        self.assertEqual(23, mini.find_minimum([530, 429449672, 97, 23, 46, 59]))


if __name__ == '__main__':
    unittest.main()

