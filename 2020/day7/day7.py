import re

# maybe this could be implemented slightly more elegant with the help of zip(), getting rid of the tuples of count and name?
# for sure, a truly recursive solution, i.e. by KanegaeGabriel [1] would have been much shorter... well, I started iteratively, so didn't mind
# and clearly, the nicest short solution credit goes to r0f1's alternative solution [2]
# [1]: https://github.com/KanegaeGabriel/advent-of-code-2020/blob/main/07_handy_haversacks.py
# [2]: https://github.com/r0f1/adventofcode2020/blob/master/day07/alt.py

# parse data
data = [line.strip() for line in open("input") if line != ""]

# pack the data inside a dict of bag names that contains a list of tuples out of count and name of the contents
bagcontent = lambda m: (int(m.groups()[0]), m.groups()[1])
bag = lambda m: (m[0], [bagcontent(re.match(r"(\d+) (.+) bags?", x)) for x in m[1].split(", ") if x != "no other bags"])
datadict = dict(bag(re.match(r"(.+) bags contain (.+)\.$", line).groups()) for line in data)

shinygold_bags = None
# get the set of bags that contain a number of shiny gold bags
updated_bags = set(k for k, c in datadict.items() if any(u[1] == "shiny gold" for u in c))
while updated_bags != shinygold_bags:
    shinygold_bags = updated_bags
    # now somewhat iteratively (until the set doesn't get extended anymore), get the set of bags that contain the current set of bags
    updated_bags = shinygold_bags.union(k for content in shinygold_bags for k, c in datadict.items() if any(u[1] == content for u in c))

# the length of these is the result
result1 = len(shinygold_bags)
print(f"part 1: {result1}")

shinygold_content = []
# in the second part, we need to keep track of all iterations so start by filling the bags that the shiny gold bags contain, to be able to sum up
updated_content = datadict["shiny gold"]
while updated_content:
    shinygold_content.append(updated_content)
    # now somewhat iteratively (until there is no more content), get the contents of the previous iteration of bags and multiply the count with the current content's count
    updated_content = [(xu * u[0], xv) for u in shinygold_content[-1] for xu, xv in datadict[u[1]]]

# sum everything together
result2 = sum(u[0] for x in shinygold_content for u in x)
print(f"part 2: {result2}")