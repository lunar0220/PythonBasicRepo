import unittest

def count_vowels(text: str) -> int:
    vowels = "aeiou"
    count = 0

    for char in text.lower():
        if char in vowels:
            count += 1
    return count

class TestCountVowels(unittest.TestCase):
    def test_regular_string(self) -> None:
        self.assertEqual(count_vowels("Hello"), 2)

    def test_mixed_case(self) -> None:
        self.assertEqual(count_vowels("AeoIu"), 5)

    def test_empty_string(self) -> None:
        self.assertEqual(count_vowels(""), 0)

    def test_no_vowels(self) -> None:
        self.assertEqual(count_vowels("bcdfgh"), 0)

    def test_sentence(self) -> None:
        self.assertEqual(count_vowels("This is a test"), 4)

if __name__ == "__main__":
    unittest.main()