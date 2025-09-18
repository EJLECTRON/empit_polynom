import unittest

from empit_polynom.polynom import Polynom


class TestPolynom(unittest.TestCase):
    def test_add_same_length(self):
        p1 = Polynom([1, 2, 3])
        p2 = Polynom([3, 2, 1])
        result = p1 + p2
        self.assertEqual(result, Polynom([4, 4, 4]))


    def test_add_different_length_1(self):
        p1 = Polynom([4, -5.5])
        p2 = Polynom([1, 2, 3])
        result = p1 + p2
        self.assertEqual(result, Polynom([5, -3.5, 3]))
        

    def test_add_different_length_2(self):
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


    def test_sub_same_length(self):
        p1 = Polynom([1, 2, 3])
        p2 = Polynom([3, 2, 1])
        result = p1 - p2
        self.assertEqual(result, Polynom([-2, 0, 2]))


    def test_sub_different_length_1(self):
        p1 = Polynom([1, 2, 3])
        p2 = Polynom([4, -5.5])
        result = p1 - p2
        self.assertEqual(result, Polynom([-3, 7.5, 3]))
    
    def test_sub_different_length_2(self):
        p1 = Polynom([-3, -432.3424352, 0, 3])
        p2 = Polynom([4, -5.5, 0, 0, 92, 12, 234])
        result = p1 - p2
        self.assertEqual(result, Polynom([-7, -426.8424352, 0, 3, -92, -12, -234]))


    def test_sub_with_empty_polynomial_1(self):
        p1 = Polynom([1, 2])
        p2 = Polynom([])
        result = p1 - p2
        self.assertEqual(result, p1)


    def test_sub_with_empty_polynomial_2(self):
        p1 = Polynom([])
        p2 = Polynom([1, 2])
        result = p1 - p2
        self.assertEqual(result, Polynom([-1, -2]))


    def test_sub_type_error(self):
        p1 = Polynom([1, 2])
        with self.assertRaises(Exception):
            _ = p1 - [1, 2]


    def test_call_evaluation(self):
        p = Polynom([1, -2, 1])
        self.assertEqual(p(3), 4)



if __name__ == "__main__":
    unittest.main()
