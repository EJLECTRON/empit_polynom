import unittest

from empit_coding_challenge.polynom import Polynom


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


class TestPolynomMultiplication(unittest.TestCase):

    # def test_mul_by_scalar(self):
    #     p = Polynom([1, -2, 3])
    #     result = p * 2
    #     self.assertEqual(result, Polynom([2, -4, 6]))

    # def test_mul_zero_scalar(self):
    #     p = Polynom([1, 2, 3])
    #     result = p * 0
    #     self.assertEqual(result, Polynom([0, 0, 0]))


    def test_mul_polynomials_simple(self):
        p1 = Polynom([1, 1])    # 1 + x
        p2 = Polynom([1, -1])   # 1 - x
        result = p1 * p2
        # (1 + x)(1 - x) = 1 - x^2
        self.assertEqual(result, Polynom([1, 0, -1]))


    def test_mul_polynomials_different_length(self):
        p1 = Polynom([2, 0, 1])   # 2 + x^2
        p2 = Polynom([1, 3])      # 1 + 3x
        result = p1 * p2
        # (2 + x^2)(1 + 3x) = 2 + 6x + x^2 + 3x^3
        self.assertEqual(result, Polynom([2, 6, 1, 3]))


    def test_mul_with_fraction_coeffs(self):
        p1 = Polynom([1/2, 1/3])  # 1/2 + (1/3)x
        p2 = Polynom([2])                               # scalar polynomial (2)
        result = p1 * p2
        self.assertEqual(result, Polynom([1, 2/3]))


    def test_mul_by_zero_polynomial(self):
        p1 = Polynom([1, 2, 3])
        p2 = Polynom([0])
        result = p1 * p2
        self.assertEqual(result, Polynom([0, 0, 0]))


    def test_mul_high_degree_polynomial(self):
        p1 = Polynom([0, 0, 1])   # x^2
        p2 = Polynom([1, 1, 1, 1])  # 1 + x + x^2 + x^3
        result = p1 * p2
        # (x^2)(1 + x + x^2 + x^3) = x^2 + x^3 + x^4 + x^5
        self.assertEqual(result, Polynom([0, 0, 1, 1, 1, 1]))


    def test_mul_large_gap_polynomial(self):
        p1 = Polynom([1, 0, 0, 5, 345, 653, -4353, 4])
        p2 = Polynom([2, 0, 3]) 
        result = p1 * p2
        self.assertEqual(result, Polynom([2, 0, 3, 10, 690, 1321, -7671, 1967, -13059, 12]))


if __name__ == "__main__":
    unittest.main()
