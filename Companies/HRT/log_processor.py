from collections import defaultdict
import heapq

_TOP_3 = 3

class LogProcessor:
	def __init__(self):
		self._code_count = defaultdict(int)
		self._urls = defaultdict(int)
	
	def process_logs(self, file_path: str):
		with open(file_path, 'r') as file:
			for line in file:
				line_strs = line.split('"')
				
				_, file_path, _ = line_strs[1].split(" ")
				status_code, _ = line_strs[2].strip().split(" ")

				self._code_count[status_code] += 1
				self._urls[file_path] += 1
	
	def sort_and_print_urls(self):
		print("Top 3 Requested Paths:")
		top_urls = heapq.nlargest(_TOP_3, self._urls.items(), key=lambda x: x[1])
		for url, freq in top_urls: print(f"{url}: {freq}")

	
	def print_status_codes(self):
		print("Status Code Counts:")

		for code, freq in self._code_count.items():
			print(f"{code}: {freq}")

if __name__ == "__main__":
	log_processor = LogProcessor()
	log_processor.process_logs("Companies/HRT/access.log")
	log_processor.print_status_codes()
	print("\n")
	log_processor.sort_and_print_urls()