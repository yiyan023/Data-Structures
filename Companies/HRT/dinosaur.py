from collections import defaultdict

class FileProcessor:
	def __init__(self):
		self._file_memory = defaultdict(int)
	
	def count_bytes(self, file_path: str):
		with open(file_path, 'r') as file:
			file_content = file.read().split("\n")
			
			for line in file_content:
				path, size, _ = line.split(",")
				dirs = path.split("/")
				assert len(dirs)

				_, file_type = dirs[-1].split(".")
				self._file_memory[file_type] += int(size)
	
	def get_file_type_bytes(self):
		res = []

		for file_type, size in self._file_memory.items():
			res.append(f"{file_type}: {size} bytes")
		
		return res

if __name__ == "__main__":
	file_processor = FileProcessor()
	file_processor.count_bytes('Companies/HRT/file.txt')
	print('\n'.join(file_processor.get_file_type_bytes()))