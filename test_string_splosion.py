import stringSplosion
import unittest
class TestStringSplosion(unittest.TestCase):

    """
        TestCases for String splosion lab
    """

    def test_string_splosion1(self):
        string_splosion = stringSplosion.StringSplosion('Code')
        self.assertEqual(
            string_splosion.manipulate(),
            'CCoCodCode',
            msg='should manipulate the string'
        )

    def test_string_splosion2(self):
        string_splosion = stringSplosion.StringSplosion('abc')
        self.assertEqual(
            string_splosion.manipulate(),
            'aababc',
            msg='should manipulate a second time'
        )

    def test_string_splosion3(self):
        string_splosion = stringSplosion.StringSplosion('andela')
        self.assertEqual(
            string_splosion.manipulate(),
            'aanandandeandelandela',
            msg='should manipulate a third time'
        )
if __name__ == '__main__':
    unittest.main()
