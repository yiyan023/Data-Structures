"""
Write a function to calculate distribution of word lengths in a text and print the corresponding histogram.

Input: a URL to a text file

Requirements: when calculating the distribution, only consider words from a word list read from a local file
"""

from collections import Counter
from sortedcontainers import SortedDict

import string
import unittest

class WordHistogram:
	def __init__(self, text_file: str):
		with open(text_file, 'r') as f:
			file_content = f.read()
			words = file_content.split()
			self.word_freq = Counter([word.strip(string.punctuation).lower() for word in words])
	
	def create_histogram(self):
		for word, freq in self.word_freq.items():
			print(f"{word}: {'*' * freq}")

if __name__ == "__main__":
	hist = WordHistogram("test.txt")
	hist.create_histogram()
