# class Robot 
# data members 
# x, y coordinates 

# functions 
# move function(cmd) -> L, R, U, D

INIT_X = 0
INIT_Y = 0
INIT_HEALTH = 10

# healht functionality 
# data member -> health 

# function:
# getHealth() 
# resetHealth() 

class Robot:
	def __init__(self, x, y, health):
		self.x = x
		self.y = y
		self.health = health
	
	def move(self, cmd):
		if cmd =="L":
			self.x -= 1
		
		elif cmd == "R":
			self.x += 1
		
		elif cmd == "U":
			self.y += 1
		
		else:
			self.y -= 1
		
		self.health -= 1
	
	def nextMove(self, cmd):
		if cmd =="L":
			return (self.x - 1, self.y)
		
		elif cmd == "R":
			return (self.x + 1, self.y)
		
		elif cmd == "U":
			return (self.x, self.y + 1)
		
		else:
			return (self.x, self.y - 1)
	
	def getHealth(self):
		return self.health 

	def resetHealth(self):
		self.health = INIT_HEALTH
	
	# testing 
	def getX(self):
		return self.x 
	
	def getY(self):
		return self.y

# room Class
# data members
# robot -> initialize charging station 
# chargin station coordinates 
# set of obstacles  s
# dimensions - height, width 

# functions 
# move robot -> out of bounds, obstacles, health of robot
	# passes all conditions -> robot.move()
	# after move, check if it is at charging station

class Room:
	def __init__(self, width, height, obstacles, charging_station):
		self.robot = Robot(charging_station[0], charging_station[1], INIT_HEALTH)
		self.charging_station = charging_station
		self.height = height 
		self.width = width
		self.obstacles = set()

		for block in obstacles:
			for x in range(block["min_x"], block["max_x"] + 1):
				for y in range(block["min_y"], block["max_y"] + 1):
					self.obstacles.add((x, y))
	
	def inRoom(self, x, y):
		return 0 <= x <= self.width and 0 <= y <= self.height

	def hasObstacle(self, x, y):
		return (x, y) in self.obstacles

	def zeroHealth(self):
		return not self.robot.getHealth()

	def atChargingStation(self, x, y):
		return [x, y] == self.charging_station
	
	def move_robot(self, cmd):
		next_x, next_y = self.robot.nextMove(cmd)

		if self.inRoom(next_x, next_y) and not self.hasObstacle(next_x, next_y) and not self.zeroHealth():
			self.robot.move(cmd)

			if self.atChargingStation(next_x, next_y):
				self.robot.resetHealth()
	
	# testing 
	def getRobotX(self):
		return self.robot.getX()

	def getRobotY(self):
		return self.robot.getY()

	def getRobotHealth(self):
		return self.robot.getHealth()


if __name__ == "__main__":
	input = {
		"room_description": {
			"room": [5, 5],
			"obstacles": [
				{ "min_x": 4, "max_x": 5, "min_y": 4, "max_y": 5 },
			],

			"charging_station": [1, 4]
		}
	}

	width, height = input["room_description"]["room"]
	obstacles = input["room_description"]["obstacles"]
	charging_station = input["room_description"	]["charging_station"]

	room = Room(width, height, obstacles, charging_station)

	# out of bounds 
	room.move_robot("L") # test for all the bounds
	room.move_robot("L")
	assert(room.getRobotX() == 0)
	assert(room.getRobotY() == 4)
	assert(room.getRobotHealth() == 9)

	# resetting health at the charging station 
	room.move_robot("R")
	assert(room.getRobotX() == 1)
	assert(room.getRobotY() == 4)
	assert(room.getRobotHealth() == 10)

	# obstacle collision 
	room.move_robot("R")
	room.move_robot("R")
	room.move_robot("R")
	assert(room.getRobotX() == 3)
	assert(room.getRobotY() == 4)
	assert(room.getRobotHealth() == 8)

	# zero health 
	room.move_robot("L") # 2, 4, 7
	room.move_robot("U") # 2, 5, 6
	room.move_robot("U") # 2, 5, 6
	room.move_robot("R") # 3, 5, 5
	room.move_robot("D") # 3, 4, 4
	room.move_robot("D") # 3, 3, 3
	room.move_robot("D") # 3, 2, 2
	room.move_robot("D") # 3, 1, 1
	room.move_robot("D") # 3, 0, 0
	room.move_robot("D") # 3, 0, 0
	assert(room.getRobotX() == 3)
	assert(room.getRobotY() == 0)
	assert(room.getRobotHealth() == 0)

	print("Assertion passed!")
