class Logger:

    def __init__(self):
        self.logger = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.logger or timestamp >= self.logger[message] + 10:
            self.logger[message] = timestamp 
            return True
        
        return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
