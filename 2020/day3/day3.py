from functools import reduce
import operator

# parse data
data = [line.strip() for line in open("input")]

# iterating over each slope y line starting on the second, add the slope x to the x coordinate and count all positions with a "#"
traverse = lambda s: sum(data[y][(y // s[1] * s[0]) % len(data[0])] == "#" for y in range(s[1], len(data), s[1])) 

# do this for the slope "x + 3, y + 1"
result1 = traverse((3, 1))
print(f"part 1: {result1}")

# do the same just for every of these slopes and multiply the results together
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
result2 = reduce(operator.mul, [traverse(x) for x in slopes])
print(f"part 2: {result2}")