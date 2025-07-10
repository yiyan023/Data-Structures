import csv

class StockProcessor:
	def __init__(self, ticker: str) -> None:
		self._ticker = ticker 
		self._acc = 0 
		self._count = 0  
		self._max_range = 0
		self._max_day = ""
	
	def process_csv(self, file_path: str):
		with open(file_path, 'r') as file:
			file_content = csv.reader(file)

			for row in file_content:
				if row[1] != self._ticker:
					continue 

				if float(row[3]) - float(row[4]) > self._max_range:
					self._max_range = float(row[3]) - float(row[4])
					self._max_day = row[0]
				
				self._acc += int(row[6])
				self._count += 1
	
	def fetch_output(self):
		average = self._acc / self._count if self._count else 0
		return [
			f"Ticker: {self._ticker}", 
			f"Date with largest price range: {self._max_day} (Range: ${round(self._max_range, 2)})",
			f"Average daily volume: {average}"
		]

if __name__ == "__main__":
	stock_processor = StockProcessor("AAPL")
	stock_processor.process_csv("Companies/HRT/stock_prices.csv")
	print('\n'.join(stock_processor.fetch_output()))
				

				



