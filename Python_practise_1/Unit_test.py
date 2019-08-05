import unittest
import Test5    

class TestRaindrops(unittest.TestCase):

    def test_1(self):
        number = 30
        result = Test5.divisible(number,5)
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()

