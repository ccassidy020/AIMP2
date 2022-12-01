from typing import Dict

from solver import Solver
from ucs import UCSSearch
from gbfsH1 import GBFSSolverH1
from gbfsH2 import GBFSSolverH2
from gbfsH3 import GBFSSolverH3
from gbfsH4 import GBFSSolverH4
from AH1 import ASolverH1
from AH2 import ASolverH2
from AH3 import ASolverH3
from AH4 import ASolverH4


if __name__ == '__main__':
	cases = [x.strip() for x in open("./generated-input5.txt", "r").readlines() if x[0] != '#' and x[0] != '\n']
	algorithms: Dict[str, Solver] = {
		"ucs": UCSSearch,
		"gbfs-h1": GBFSSolverH1,
		"gbfs-h2": GBFSSolverH2,
		"gbfs-h3": GBFSSolverH3,
		"gbfs-h4": GBFSSolverH4,
		"a-h1": ASolverH1,
		"a-h2": ASolverH2,
		"a-h3": ASolverH3,
		"a-h4": ASolverH4
	}
	for algorithm in algorithms:
		for i, case in enumerate(cases):
			print(i)
			s = algorithms[algorithm](case)
			open("./output/{:}-sol-{:}.txt".format(algorithm, str(i + 1)), "w").write(s.out)
			open("./output/{:}-search-{:}.txt".format(algorithm, str(i + 1)), "w").write(s.out_search)
