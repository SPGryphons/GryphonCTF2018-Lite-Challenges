#!/usr/bin/env python3
import re, socket

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

def main():
	conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	conn.connect(("0.0.0.0", 50000))
	conn.recv(2048)
	conn.sendall("\n".encode())

	while True:
		mazeLevel = conn.recv(10240).decode()
		pattern = re.match("\s+\w+\s\w+:\s(\W+)", mazeLevel)

		if pattern:
			solution = getSoln(pattern.group(1).strip())
			conn.sendall(solution.encode())
		elif not mazeLevel:
			break
		else:
			print(mazeLevel)

def getSoln(pattern):
	pattern = re.split("\n", pattern)
	pattern = [list(row) for row in pattern]
	sides = len(pattern)
	found = False

	for row in range(0, sides):
		for col in range(0, sides):
			if pattern[row][col] == "@":
				found = True
				break
		if found:
			break

	solution = pollAll(pattern, row, col, [""])
	return solution

def pollAll(maze, row, col, lastMoves):
	movesPossible = moveOptions[lastMoves[len(lastMoves) - 1]]
	startRow, startCol = row, col
	newRow, newCol = [0 for _ in range(0, 2)]
	out = ""

	for move in movesPossible:
		newRow, newCol = nextBlock(row, col, move)
		try:
			if maze[newRow][newCol] == "░":
				lastMoves.append(move)
				pollAll(maze, newRow, newCol, lastMoves)
		except:
			break

	for move in lastMoves:
		if move == "":
			continue
		else:
			out += moveDir[move] + " "

	return out.strip()

def nextBlock(row, col, move):
	if move == 0:
		row -= 1
	elif move == 1:
		col += 1
	elif move == 2:
		row += 1
	elif move == 3:
		col -= 1

	return (row, col)

if __name__ == "__main__":
	main()