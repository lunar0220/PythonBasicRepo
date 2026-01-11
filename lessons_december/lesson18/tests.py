import datetime
import math
import random
import unittest

import pandas


def devide(num_1: int, num_2: int) -> float | None:
    if num_2 == 0:
        raise ValueError(f"Param num_2 can't be 0")
    return num_1 / num_2


class TestDevideFunction(unittest.TestCase):
    def test_success(self) -> None:
        self.assertEqual(devide(10, 2), 5)

    def test_value_error(self) -> None:
        self.assertRaises(ValueError, devide, 10, 0)

    def test_type_error(self) -> None:
        self.assertRaises(TypeError, devide, 10, "!")


if __name__ == "__main__":
    unittest.main()
