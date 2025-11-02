"""Utility examples for practice6 - file1

This file contains several small utility functions (math, strings, I/O)
and a simple demonstration when run as a script. Each function is
documented and the file intentionally contains more than 50 lines.
"""
from typing import List, Tuple, Iterable
import json
import math


def fibonacci(n: int) -> int:
	"""Return the n-th Fibonacci number (0-indexed).

	Uses an iterative approach (O(n) time, O(1) memory).
	"""
	if n <= 0:
		return 0
	if n == 1:
		return 1
	a, b = 0, 1
	for _ in range(2, n + 1):
		a, b = b, a + b
	return b


def is_prime(num: int) -> bool:
	"""Return True if num is a prime number, False otherwise."""
	if num < 2:
		return False
	if num % 2 == 0:
		return num == 2
	limit = int(math.isqrt(num))
	for i in range(3, limit + 1, 2):
		if num % i == 0:
			return False
	return True


def primes_in_range(start: int, end: int) -> List[int]:
	"""Return all prime numbers in [start, end] (inclusive)."""
	if start > end:
		return []
	return [p for p in range(max(2, start), end + 1) if is_prime(p)]


def reverse_words(s: str) -> str:
	"""Reverse the order of words in a string, keeping whitespace trimmed."""
	parts = s.strip().split()
	return " ".join(reversed(parts))


def normalize_whitespace(s: str) -> str:
	"""Collapse multiple spaces/tabs/newlines into single spaces."""
	return " ".join(s.split())


def histogram(values: Iterable[int]) -> dict:
	"""Return a histogram (value -> count) for an iterable of ints."""
	hist = {}
	for v in values:
		hist[v] = hist.get(v, 0) + 1
	return hist


def save_json(path: str, obj) -> None:
	"""Save an object to path as pretty JSON."""
	with open(path, "w", encoding="utf-8") as f:
		json.dump(obj, f, ensure_ascii=False, indent=2)


def load_json(path: str):
	"""Load JSON object from a file and return it."""
	with open(path, "r", encoding="utf-8") as f:
		return json.load(f)


def chunked(seq: List, size: int) -> List[List]:
	"""Split a list into chunks of given size (last chunk may be smaller)."""
	if size <= 0:
		raise ValueError("size must be > 0")
	return [seq[i : i + size] for i in range(0, len(seq), size)]


def demo() -> None:
	"""Run a short demo printing outputs of utilities."""
	print("file1.py demo: math + text utilities")
	print("Fibonacci numbers (first 10):", [fibonacci(i) for i in range(10)])
	print("Primes from 1..30:", primes_in_range(1, 30))
	sample = "  Hello   world!  This is   file1.  "
	print("Original:", repr(sample))
	print("Normalized:", repr(normalize_whitespace(sample)))
	print("Reversed words:", reverse_words(sample))
	values = [1, 2, 2, 3, 3, 3]
	print("Histogram:", histogram(values))
	print("Chunked sample [0..9] into 3:", chunked(list(range(10)), 3))


if __name__ == "__main__":
	demo()
 

"""
This is some changed text for task 1 for file1.py dgsadgdsbdsbdsbdsbds
This is some changed text for task 1 for file1.py fbghfsdbsnsdfnsd
"""
