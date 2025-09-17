import unittest

from empit_polynom.polynom import Polynom


class TestPolynom(unittest.TestCase):
    def test_add_same_length(self):
        p1 = Polynom([1, 2, 3])
        p2 = Polynom([3, 2, 1])
        result = p1 + p2
        self.assertEqual(result, Polynom([4, 4, 4]))


    def test_add_different_length(self):
        p1 = Polynom([1, 2, 3])
        p2 = Polynom([4, -5.5])
        result = p1 + p2
        self.assertEqual(result, Polynom([5, -3.5, 3]))


    def test_add_with_empty_polynomial(self):
        p1 = Polynom([1, 2])
        p2 = Polynom([])
        result = p1 + p2
        self.assertEqual(result, p1)


    def test_add_type_error(self):
        p1 = Polynom([1, 2])
        with self.assertRaises(Exception):
            _ = p1 + [1, 2]


    def test_call_evaluation(self):
        p = Polynom([1, -2, 1])
        self.assertEqual(p(3), 4)



if __name__ == "__main__":
    unittest.main()
