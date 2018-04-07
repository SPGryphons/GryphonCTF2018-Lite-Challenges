#!/usr/bin/env python3
import random, sys

moveDir = {
	0 : "up",
	1 : "right",
	2 : "down",
	3 : "left"
}

moveOptions = {
	"" : [0, 1, 2, 3],
	0 : [0, 1, 3],
	1 : [0, 1, 2],
	2 : [1, 2, 3],
	3 : [0, 2, 3]
}

class Blocks:
	def __init__(self, row, col):
		self.__fill = chr(9619)
		self.__visited = False

	# True means block cannot be "visited"
	def poll(self):
		return self.__visited

	def setFill(self, fill):
		self.__fill = fill
		self.__visited = True

	def getFill(self):
		return self.__fill

class Maze:
	# [1, 2, 3] row = 0
	# [4, 5, 6] row = 1
	# [7, 8, 9]
	# row horizontal
	# col vertical

	def __init__(self, sides):
		self.__sides = sides
		self.__mazePattern = [[Blocks(row, col) for col in range(0, sides)] for row in range(0, sides)]
		# Taken from a vertical perspective
		topOffset = int(sides / 3)
		bottomOffset = sides - topOffset

		self.__startRow = random.randint(topOffset, bottomOffset)
		self.__startCol = random.randint(topOffset, bottomOffset)

		self.__mazePattern[self.__startRow][self.__startCol].setFill("@")
		self.__generate()

	def __generate(self):
		self.__currRow = self.__startRow
		self.__currCol = self.__startCol
		self.__solution = []
		lastMove = ""

		while self.__currRow != 0\
		and self.__currRow != self.__sides - 1\
		and self.__currCol != 0\
		and self.__currCol != self.__sides - 1:
			movesPossible = moveOptions[lastMove]
			removalList = []

			for move in movesPossible:
				moveBoolean, movedRow, movedCol = self.__pollBlock(self.__currRow, self.__currCol, move)
				if moveBoolean:
					removalList.append(move)
					continue
				else:
					if self.__pollAll(movedRow, movedCol, moveOptions[move]):
						removalList.append(move)

			for move in removalList:
				movesPossible.remove(move)

			lastMove = self.__move(movesPossible)
			self.__solution.append(lastMove)

	def __move(self, movesPossible):
		move = movesPossible[random.randint(0, len(movesPossible) - 1)]

		if move == 0:
			self.__currRow -= 1
		elif move == 1:
			self.__currCol += 1
		elif move == 2:
			self.__currRow += 1
		elif move == 3:
			self.__currCol -= 1

		self.__mazePattern[self.__currRow][self.__currCol].setFill(chr(9617))

		return move

	def __pollBlock(self, row, col, move):
		if move == 0:
			row -= 1
		elif move == 1:
			col += 1
		elif move == 2:
			row += 1
		elif move == 3:
			col -= 1

		return (self.__mazePattern[row][col].poll(), row, col)

	def __pollAll(self, row, col, movesPossible):
		boolList = []

		for move in movesPossible:
			try:
				moveBoolean, *_ = self.__pollBlock(row, col, move)
				boolList.append(moveBoolean)
			except:
				pass

		if True in boolList:
			return True

		return False

	def getSolution(self):
		out = ""
		
		for x in self.__solution:
			out += moveDir[x] + " "

		return out.strip()
	
	def getMaze(self):
		msg = ""
		for row in self.__mazePattern:
			for item in row:
				msg += item.getFill()
			msg += "\n"

		return msg[:-1]

def main():
	MazeObj = Maze(9)
	MazeObj.print()
	print(MazeObj.getSolution())

if __name__ == "__main__":
	main()