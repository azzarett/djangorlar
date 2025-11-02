"""Utility examples for practice6 - file2

Contains collection utilities, simple data classes, and algorithms.
"""
from dataclasses import dataclass, field
from typing import List, Iterable, Any
import random


def merge_sort(arr: List[Any]) -> List[Any]:
	"""Return a new sorted list using merge sort."""
	if len(arr) <= 1:
		return arr[:]
	mid = len(arr) // 2
	left = merge_sort(arr[:mid])
	right = merge_sort(arr[mid:])
	return _merge(left, right)


def _merge(left: List[Any], right: List[Any]) -> List[Any]:
	result = []
	i = j = 0
	while i < len(left) and j < len(right):
		if left[i] <= right[j]:
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1
	result.extend(left[i:])
	result.extend(right[j:])
	return result


def reservoir_sample(iterable: Iterable[Any], k: int) -> List[Any]:
	"""Randomly sample k items from iterable using reservoir sampling.

	Works in O(n) time and O(k) memory and supports large or streaming inputs.
	"""
	if k <= 0:
		return []
	reservoir = []
	for i, item in enumerate(iterable, start=1):
		if i <= k:
			reservoir.append(item)
		else:
			j = random.randrange(0, i)
			if j < k:
				reservoir[j] = item
	return reservoir


def unique_preserve_order(seq: Iterable[Any]) -> List[Any]:
	"""Return unique elements while preserving original order."""
	seen = set()
	result = []
	for x in seq:
		if x not in seen:
			seen.add(x)
			result.append(x)
	return result


@dataclass
class Student:
	name: str
	age: int
	student_id: str
	grades: List[int] = field(default_factory=list)

	def add_grade(self, grade: int) -> None:
		if not 0 <= grade <= 100:
			raise ValueError("grade must be between 0 and 100")
		self.grades.append(grade)

	def average(self) -> float:
		if not self.grades:
			return 0.0
		return sum(self.grades) / len(self.grades)

	def __str__(self) -> str:
		return f"Student({self.name}, id={self.student_id}, avg={self.average():.2f})"


def demo_collections() -> None:
	print("file2.py demo: collections + sampling + sorting")
	arr = [random.randint(0, 50) for _ in range(20)]
	print("original:", arr)
	print("merge_sorted:", merge_sort(arr))
	print("unique_preserve_order:", unique_preserve_order([1, 2, 1, 3, 2, 4, 3]))
	print("reservoir sample 5:", reservoir_sample(range(100), 5))


def demo_students() -> None:
	print("\nfile2.py demo: Student dataclass")
	s = Student("Alina", 21, "S100")
	for g in [88, 92, 75, 100]:
		s.add_grade(g)
	print(s)


if __name__ == "__main__":
	demo_collections()
	demo_students()
 
"""f
this is also some changed text for task 1fdsfdsafsdafsadfa
"""
"""
vvvvvvvvvvvvvvvvv
this is
this is also some changed 
"""

