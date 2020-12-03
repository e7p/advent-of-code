import itertools
from functools import reduce
import operator

# parse data
data = [int(line) for line in open("input")]

# for each combination of n elements, check if they sum to 2020, and if, return the multiplication of these
checkmul = lambda n: [reduce(operator.mul, x) for x in itertools.combinations(data, n) if sum(x) == 2020]

# do this for n = 2
result1 = checkmul(2)
print(f"part 1: {result1}")

# do this for n = 3
result2 = checkmul(3)
print(f"part 2: {result2}")