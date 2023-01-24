import unittest
from parameterized import parameterized
from Teme_ITF.Tema_8.app.tema8_1 import is_even, list_of_positives, compare_nr_of


class TestTema8_1(unittest.TestCase):

    def test_def_is_even_True(self):
        self.assertEqual(is_even(4), True)

    def test_def_is_even_False(self):
        self.assertEqual(is_even(5), False)

    @parameterized.expand([
        (4, True),
        (5, False)
    ])
    def test_def_is_even(self, n, expected):
        self.assertEqual(is_even(n), expected)

    @parameterized.expand([
        ([3, 2, -1], [3, 2]),
        ([-10, 1, 15, 0], [1, 15]),
        ([-2, 0, -5], [])
    ])
    def test_list_of_positives(self, lst, expected):
        self.assertEqual(list_of_positives(lst), expected)

    def test_compare_nr_of_no1(self):
        self.assertEqual(compare_nr_of(5, 3), 5)

    def test_compare_nr_of_no2(self):
        self.assertEqual(compare_nr_of(3, 6), 6)

    def test_compare_nr_of_equal(self):
        self.assertEqual(compare_nr_of(3, 3), None)

    @parameterized.expand([
        (5, 3, 5),
        (3, 5, 5),
        (3, 3, None)])
    def test_compare_nr_of(self, n, z, expected):
        self.assertEqual(compare_nr_of(n, z), expected)
