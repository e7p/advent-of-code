# parse data
data = [line.strip() for line in open("input")]

# to keep straightforward, the seat ID generates directly from the binary conversion of the "FBLR" encoded string
seat_ids = [int(x.translate(str.maketrans("FBLR", "0101")), 2) for x in data]

# just take the maximum value there
result1 = max(seat_ids)
print(f"part 1: {result1}")

# iterate over each possible seat ID which can have a predecessor or sucessor and only select those that are unoccupied
result2 = [i for i in range(min(seat_ids) + 1, result1) if i not in seat_ids]
print(f"part 2: {result2}")