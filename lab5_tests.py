import data
import lab5
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    #    Part 1 tests should be in data_tests.py.
    class TestTime(unittest.TestCase):

        def test_time_equality_same_attributes(self):
            time1 = Time(10, 30, 25)
            time2 = Time(10, 30, 25)
            self.assertEqual(time1, time2)

        def test_time_inequality_different_attributes(self):
            time1 = Time(10, 30, 25)
            time2 = Time(11, 30, 25)
            time3 = Time(10, 31, 25)
            time4 = Time(10, 30, 26)
            self.assertNotEqual(time1, time2)
            self.assertNotEqual(time1, time3)
            self.assertNotEqual(time1, time4)

        def test_time_inequality_different_type(self):
            time1 = Time(10, 30, 25)
            not_a_time = (10, 30, 25)
            self.assertNotEqual(time1, not_a_time)

    if __name__ == '__main__':
        unittest.main()
    # Part 2
    #    Part 2 tests should be in data_tests.py.
    class TestTime(unittest.TestCase):

        def test_time_equality_same_attributes(self):
            time1 = Time(10, 30, 25)
            time2 = Time(10, 30, 25)
            self.assertEqual(time1, time2)

        def test_time_inequality_different_attributes(self):
            time1 = Time(10, 30, 25)
            time2 = Time(11, 30, 25)  # Different hour
            time3 = Time(10, 31, 25)  # Different minute
            time4 = Time(10, 30, 26)  # Different second
            self.assertNotEqual(time1, time2)
            self.assertNotEqual(time1, time3)
            self.assertNotEqual(time1, time4)

        def test_time_inequality_different_type(self):
            time1 = Time(10, 30, 25)
            not_a_time = (10, 30, 25)  # Tuple, not a `Time` object
            self.assertNotEqual(time1, not_a_time)

        def test_time_repr(self):
            time = Time(10, 30, 25)
            expected_repr = "Time(hour=10, minute=30, second=25)"
            self.assertEqual(repr(time), expected_repr)

    # Part 3
    def test_time_add_no_carry(self):
        time1 = Time(1, 20, 15)
        time2 = Time(2, 10, 25)
        result = time_add(time1, time2)
        expected = Time(3, 30, 40)
        self.assertEqual(result, expected)

    def test_time_add_with_carry(self):
        time1 = Time(1, 59, 50)
        time2 = Time(2, 1, 15)
        result = time_add(time1, time2)
        expected = Time(4, 1, 5)
        self.assertEqual(result, expected)

    # Part 4
    class TestIsDescending(unittest.TestCase):

        def test_descending_order(self):
            self.assertTrue(is_descending([5.5, 4.4, 3.3, 2.2, 1.1]))

        def test_not_descending_order(self):
            self.assertFalse(is_descending([5.5, 5.0, 3.3, 2.2, 1.1]))

        def test_single_element_list(self):
            self.assertTrue(is_descending([5.0]))

        def test_empty_list(self):
            self.assertTrue(is_descending([]))

        def test_mixed_order(self):
            self.assertFalse(is_descending([5.5, 4.4, 6.6, 2.2]))

    # Part 5
    def largest_between(numbers: List[int], lower: int, upper: int) -> Optional[int]:
        if lower > upper:
            return None

        lower = max(0, lower)
        upper = min(len(numbers) - 1, upper)

        max_index = lower
        for i in range(lower, upper + 1):
            if numbers[i] > numbers[max_index]:
                max_index = i

        return max_index

    # Part 6
class TestFurthestFromOrigin(unittest.TestCase):

    def test_multiple_points(self):
        # Test with multiple points, expecting the index of the furthest point
        points = [Point(1, 1), Point(2, 2), Point(3, 3), Point(0, 4)]
        self.assertEqual(furthest_from_origin(points), 3)  # (0, 4) is furthest from (0,0)

    def test_single_point(self):
        # Test with a single point, expecting index 0
        points = [Point(5, 5)]
        self.assertEqual(furthest_from_origin(points), 0)

    def test_empty_list(self):
        # Test with an empty list, expecting None
        points = []
        self.assertIsNone(furthest_from_origin(points))

    def test_all_same_distance(self):
        # Test where all points are equidistant from the origin
        points = [Point(3, 4), Point(-3, 4), Point(4, 3)]
        self.assertEqual(furthest_from_origin(points), 0)  # All have the same distance; return the first index





if __name__ == '__main__':
    unittest.main()
