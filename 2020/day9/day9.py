from itertools import combinations, accumulate

# parse data
data = [int(line.strip()) for line in open("input")]

# if there is no two elements in the previous 25 elements starting from the 25th element that sum to the current element, return it
result1 = [data[i] for i in range(25, len(data)) if not any(data[i] == sum(c) for c in combinations(data[i-25:i], 2))]

print(f"part 1: {result1}")

# return the sum of minimum and maximum of the sequence that sums to the result of the first part, given that the sequence is longer than 1
result2 = [min(data[i:i+x+1]) + max(data[i:i+x+1]) for i in range(len(data)) for x, k in enumerate(accumulate(data[i:])) if k == result1[0] and x > 0]

print(f"part 2: {result2}")