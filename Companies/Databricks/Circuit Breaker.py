"""
The task is to simulate a circuit breaker. The setup includes a primary server and a secondary server. You need to simulate a circuit breaker mechanism: for example, if the primary server fails, retry with the secondary server. If a server fails consecutively a certain number of times, it should be directly rejected, and after being rejected for a certain number of times, it should become eligible for retry again.
"""

import random

class Server:
    def __init__(self, fail_rate: float, fail_max: int, reject_max: int):
        self.fail_rate = fail_rate
        self.fail_count = 0
        self.reject_count = 0
        self.reject_max = reject_max
        self.fail_max = fail_max
        self.rejectMode = False
    
    def return_request_status(self):
        if self.rejectMode:
            self.reject_count += 1

            if self.reject_count >= self.reject_max:
                self.reject_count = 0
                self.rejectMode = False 
            
            return False
        
        else:
            success = (not random.random() < self.fail_rate)

            if not success:
                self.fail_count += 1

                if self.fail_count >= self.fail_max:
                    self.rejectMode = True 
                    self.fail_count = 0
            
            return success

class CircuitBreaker:
    def __init__(self, fail_rate: float, fail_max: int, reject_max: int):
        self.server_a = Server(fail_rate, fail_max, reject_max)
        self.server_b = Server(fail_rate, fail_max, reject_max)
    
    def make_request(self):
        request_status = self.server_a.return_request_status()
        is_primary_server = False 

        while not request_status:
            request_status = self.server_a.return_request_status() if is_primary_server else self.server_b.return_request_status()
            is_primary_server = not is_primary_server
        
        return request_status
            
