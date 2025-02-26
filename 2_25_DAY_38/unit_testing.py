import unittest
import pylint_for_test

class TestCap(unittest.TestCase):
    def test_one_word(self):
        t = 'python'
        result = pylint_for_test.cap_text(t)
        self.assertEqual(result,'Python')

    def test_multipal_word(self):
        t = 'python programming'
        result = pylint_for_test.cap_text(t)
        print(result)
        self.assertEqual(result , 'Python programming')
        print(result)

if __name__ == '__main__':
    unittest.main()