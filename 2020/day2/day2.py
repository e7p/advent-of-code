import re

# parse data
data = [re.match(r"(\d+)-(\d+) (.): (.+)$", line).groups() for line in open("input")]

# count all elements that match the condition that the single character occurs at least first element times and at most second element times in the right part
result1 = sum(x[3].count(x[2]) >= int(x[0]) and x[3].count(x[2]) <= int(x[1]) for x in data)
print(f"part 1: {result1}")

# count all elements that match the condition that the single character occurs either at position first element or at position second element in the right part
result2 = sum((x[3][int(x[0]) - 1] == x[2]) ^ (x[3][int(x[1]) - 1] == x[2]) for x in data)
print(f"part 2: {result2}")