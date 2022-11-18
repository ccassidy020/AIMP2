from rush_hour import RushHour

if __name__ == '__main__':
	print([x.strip() for x in open("./sample-input.txt", "r").readlines() if x[0] != '#' and x[0] != '\n'])