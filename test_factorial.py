class FactorialTest(TestCase):
    """docstring for FactorialTest"""

    def test_constant_factorial(self):
        self.assertEqual(2,
                         factorial(2),
                         msg='2 factorial should be 2')

    def test_simple_factorial(self):
        self.assertEqual(120,
                         factorial(5),
                         msg='5 factorial should be 120')

    def test_hard_factorial(self):
        self.assertEqual(3628800,
                         factorial(10),
                         msg='10 factorial should be 3628800')
