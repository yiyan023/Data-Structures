from collections import defaultdict
import csv

class TradeLogAggregator:
	def __init__(self):
		self._daily_totals = defaultdict(int)
		self._exchange_daily_totals = defaultdict(int)
	
	def read_csv(self, file_path: str):
		with open(file_path, 'r') as file:
			file_content = list(csv.reader(file))[1:]
			file_content.sort(key= lambda x: int(x[0]))
			
			for row in file_content:
				trader_type = row[1].split("_")[0]
			
				self._daily_totals[row[0]] += int(row[4])
				self._exchange_daily_totals[(row[0], trader_type)] += int(row[4])
	
	def get_daily_totals(self):
		daily_totals = ["Daily Totals:"]
		
		for day, size in self._daily_totals.items():
			daily_totals.append(f"{day}: {size} bytes")
		
		return daily_totals
	
	def get_exchange_daily_totals(self):
		exchange_totals = ["Exchange Daily Totals:"]

		for (day, trader), size in self._exchange_daily_totals.items():
			exchange_totals.append(f"{day},{trader},{size} bytes")
		
		return exchange_totals

if __name__ == "__main__":
	trade_log_aggregator = TradeLogAggregator()
	trade_log_aggregator.read_csv('Companies/HRT/logs.csv')
	print('\n'.join(trade_log_aggregator.get_daily_totals()))
	print('\n')
	print('\n'.join(trade_log_aggregator.get_exchange_daily_totals()))