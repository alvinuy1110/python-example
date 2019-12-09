import unittest

class MyTestCase(unittest.TestCase):
    # def test_something(self):
    #     self.assertEqual(True, False)

    def test_sum(self):
        assert sum([1, 2, 3]) == 6, "Should be 6"


if __name__ == '__main__':
    unittest.main()
