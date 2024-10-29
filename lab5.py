
import data

# Write your functions for each part in the space below.

# Part 1
   # The function for Part 1 should be within the class in data.py.

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
   # The function for Part 2 should be within the class in data.py.
from typing import Any

class Time:
    # Initialize a new Time object.
    # input: hour as an int
    # input: minute as an int
    # input: second as an int
    def __init__(self, hour: int, minute: int, second: int):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __eq__(self, other: Any) -> bool:
        # Check if `other` is of type `Time`
        if type(other) != Time:
            return False
        # Check if all attributes match
        return (self.hour == other.hour and
                self.minute == other.minute and
                self.second == other.second)

    def __repr__(self) -> str:
        # Return a string that shows how the object can be created
        return f"Time(hour={self.hour}, minute={self.minute}, second={self.second})"


# Part 3
def time_add(time1: Time, time2: Time) -> Time:
    total_seconds = time1.second + time2.second
    carry_minutes, new_seconds = divmod(total_seconds, 60)

    total_minutes = time1.minute + time2.minute + carry_minutes
    carry_hours, new_minutes = divmod(total_minutes, 60)

    new_hours = time1.hour + time2.hour + carry_hours

    return Time(new_hours, new_minutes, new_seconds)
#test_time_add_no_carry: Verifies that time_add correctly sums
# two times without requiring any carry-over in seconds or minutes.

#test_time_add_with_carry: Tests time_add with values that cause
# carry-over in both seconds and minutes, ensuring that the function handles overflow correctly.

# Part 4
def is_descending(lst: List[float]) -> bool:
    # Check each pair of elements in the list
    for i in range(1, len(lst)):
        if lst[i] >= lst[i - 1]:  # If any element is not less than the previous
            return False
    return True

# Part 5
class TestLargestBetween(unittest.TestCase):

    def test_within_bounds(self):
        # Standard case where all indices are within bounds and lower <= upper
        numbers = [1, 3, 5, 7, 9, 11]
        self.assertEqual(largest_between(numbers, 1, 4), 4)  # 9 is largest between indexes 1 and 4

    def test_reverse_indices(self):
        # Case where lower > upper should return None
        numbers = [1, 3, 5, 7, 9]
        self.assertIsNone(largest_between(numbers, 4, 1))

    def test_out_of_bounds_lower(self):
        # Case where lower is out of bounds (negative)
        numbers = [1, 3, 5, 7, 9]
        self.assertEqual(largest_between(numbers, -2, 3), 3)  # 7 is largest between index 0 and 3



# Part 6
def furthest_from_origin(points: List[Point]) -> Optional[int]:
    if not points:  # Return None if the list is empty
        return None

    furthest_index = 0
    max_distance = points[0].x ** 2 + points[0].y ** 2

    for i in range(1, len(points)):
        distance = points[i].x ** 2 + points[i].y ** 2
        if distance > max_distance:
            max_distance = distance
            furthest_index = i

    return furthest_index
