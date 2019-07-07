class TestStringLength(TestCase):

    """
        TestCases for String Lengths returned in a list.
    """

    def test_string_length1(self):
        length = string_length('Godson')
        self.assertListEqual(
            [6],
            length,
            msg='should return [6] for `Godson`'
        )

    def test_string_length2(self):
        length = string_length('Mia')
        self.assertListEqual(
            [3],
            length,
            msg='should return [3] for `Mia`'
        )

    def test_string_length3(self):
        length = string_length('Mia')
        self.assertListEqual(
            [3],
            length,
            msg='should return [3] for `Mia`'
        )

    def test_string_length4(self):
        length = string_length(['Adam', 'Frankel'])
        self.assertListEqual(
            [4, 7],
            length,
            msg="should return [4, 7] for ['Adam', 'Frankel']"
        )

    def test_string_length5(self):
        length = string_length(['Michael', 'William', 'Smith'])
        self.assertListEqual(
            [7, 7, 5],
            length,
            msg="should return [7, 7, 5] for ['Michael', 'William', 'Smith']"
        )
