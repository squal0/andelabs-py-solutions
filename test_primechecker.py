import primechecker
import unittest
class PrimeNumberTest(unittest.TestCase):
    """docstring for PrimeNumberTest"""

    def test_object_type(self):
        obj = primechecker.PrimeChecker()
        self.assertEqual(True, type(obj) is primechecker.PrimeChecker,
                         msg='should be of type `PrimeChecker`')

    def test_obj_instance(self):
        obj = primechecker.PrimeChecker()
        self.assertIsInstance(obj,
                              primechecker.PrimeChecker,
                              msg='should be an instance of `PrimeChecker`')

    def test_is_prime_one(self):
        prime = primechecker.PrimeChecker('41')
        self.assertEqual(True,
                         prime.is_prime(),
                         msg='should return true for 41')

    def test_is_prime_two(self):
        prime = primechecker.PrimeChecker('101')
        self.assertEqual(True,
                         prime.is_prime(),
                         msg='should return true for 101')

    def test_is_prime_three(self):
        prime = primechecker.PrimeChecker('67')
        self.assertEqual(True,
                         prime.is_prime(),
                         msg='should return false for 68')

    def test_is_prime_four(self):
        prime = primechecker.PrimeChecker('3')
        self.assertEqual(True,
                         prime.is_prime(),
                         msg='should return true for 41')

    def test_is_prime_five(self):
        prime = primechecker.PrimeChecker('')
        self.assertEqual(False,
                         prime.is_prime(),
                         msg='should return false for ""')

if __name__ == '__main__':
    unittest.main()
