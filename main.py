from typing import Dict

from solver import Solver
from ucs import UCSSearch

if __name__ == '__main__':
	cases = [x.strip() for x in open("./sample-input.txt", "r").readlines() if x[0] != '#' and x[0] != '\n']
	algorithms: Dict[str, Solver] = {
		"ucs": UCSSearch
	}
	for algorithm in algorithms:
		for i, case in enumerate(cases):
			s = algorithms[algorithm](case)
			open("./output/{:}-sol-{:}.txt".format(algorithm, str(i + 1)), "w").write(s.out)
			open("./output/{:}-search-{:}.txt".format(algorithm, str(i + 1)), "w").write(s.out_search)
