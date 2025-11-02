"""Utility examples for practice6 - file3

This file provides miscellaneous utilities: date helpers, string tools,
conversion functions and a small password generator/demo. It's intentionally
over 50 lines to satisfy practice requirements.
"""
from typing import List, Tuple
import datetime
import random
import string


def calculate_age(birth_year: int, birthday_month: int = 1, birthday_day: int = 1) -> int:
	"""Return approximate age given birth date components.

	Uses the current date; returns an integer age in years.
	"""
	today = datetime.date.today()
	try:
		bday = datetime.date(birth_year, birthday_month, birthday_day)
	except Exception:
		# fallback: use Jan 1 of birth_year when invalid month/day
		bday = datetime.date(birth_year, 1, 1)
	years = today.year - bday.year
	if (today.month, today.day) < (bday.month, bday.day):
		years -= 1
	return years


def is_leap_year(year: int) -> bool:
	"""Return True if year is a leap year."""
	return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def generate_multiplication_table(number: int, max_multiplier: int = 10) -> List[str]:
	"""Return a multiplication table (as list of strings) for number."""
	return [f"{number} x {i} = {number * i}" for i in range(1, max_multiplier + 1)]


def find_max_min(numbers: List[float]) -> Tuple[float, float]:
	"""Return max and min of a list. If empty, return (None, None)."""
	if not numbers:
		return None, None
	return max(numbers), min(numbers)


def count_words(text: str) -> int:
	"""Return number of words in text (simple whitespace split)."""
	return len(text.split())


def remove_duplicates_preserve(lst: List) -> List:
	"""Remove duplicates while preserving order."""
	seen = set()
	out = []
	for x in lst:
		if x not in seen:
			seen.add(x)
			out.append(x)
	return out


def celsius_to_fahrenheit(celsius: float) -> float:
	return (celsius * 9.0 / 5.0) + 32.0


def fahrenheit_to_celsius(fahrenheit: float) -> float:
	return (fahrenheit - 32.0) * 5.0 / 9.0


def calculate_bmi(weight_kg: float, height_m: float) -> float:
	"""Return BMI rounded to 2 decimals; raises ValueError for non-positive height."""
	if height_m <= 0:
		raise ValueError("height_m must be > 0")
	bmi = weight_kg / (height_m ** 2)
	return round(bmi, 2)


def get_bmi_category(bmi: float) -> str:
	if bmi < 18.5:
		return "Underweight"
	if bmi < 25:
		return "Normal"
	if bmi < 30:
		return "Overweight"
	return "Obese"


def generate_password(length: int = 12, use_punctuation: bool = True) -> str:
	"""Generate a random password with given length."""
	if length <= 0:
		raise ValueError("length must be positive")
	chars = string.ascii_letters + string.digits
	if use_punctuation:
		chars += string.punctuation
	return ''.join(random.choice(chars) for _ in range(length))


def demo_misc() -> None:
	print("file3.py demo: misc utilities")
	print("Age for 1990-06-15:", calculate_age(1990, 6, 15))
	print("Leap years sample:", [y for y in range(1998, 2026) if is_leap_year(y)])
	print("Multiplication table for 7:")
	for line in generate_multiplication_table(7, 5):
		print(" ", line)
	numbers = [3.5, 2.1, 9.8, 3.5]
	print("Max, Min:", find_max_min(numbers))
	text = "This   is a test.  Count   words!"
	print("Word count:", count_words(text))
	print("Remove duplicates:", remove_duplicates_preserve([1, 2, 1, 3, 2, 4]))
	print("25C -> F:", celsius_to_fahrenheit(25))
	print("77F -> C:", fahrenheit_to_celsius(77))
	bmi = calculate_bmi(70, 1.75)
	print(f"BMI: {bmi}, category: {get_bmi_category(bmi)}")
	print("Sample password:", generate_password(12))


if __name__ == "__main__":
	demo_misc()
 
"""
This is some changed text for task 1 for file3.py for branch 5
"""

