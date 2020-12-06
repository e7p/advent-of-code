# parse data
data = [line.strip() for line in open("input").read().split("\n\n")]

# sum up all unique characters in each block, excluding the newlines separating each answer
result1 = sum(len(set(x.replace("\n", ""))) for x in data)
print(f"part 1: {result1}")

# sum up all characters that are in all answers of every block by iterating through the first answer's characters 
result2 = sum(sum(all(y in x for x in z.split("\n")) for y in z.split("\n")[0]) for z in data)
print(f"part 2: {result2}")