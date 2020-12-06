import re

# parse data
data = [dict([x.split(":") for x in y.split()]) for y in open("input").read().split("\n\n")]

# dictionary of required keys with an attached tuple of rules for the values in form of a regular expression followed by integer ranges for matching groups
required_keys = {
    "byr": (r"(\d{4})$", (1920, 2002)),
    "iyr": (r"(\d{4})$", (2010, 2020)),
    "eyr": (r"(\d{4})$", (2020, 2030)),
    "hgt": (r"(?:(\d+)cm|(\d+)in)$", (150, 193), (59, 76)),
    "hcl": (r"#[0-9a-f]{6}$",),
    "ecl": (r"(?:amb|blu|brn|gry|grn|hzl|oth)$",),
    "pid": (r"\d{9}$",)
}

# counts all entries that have as much keys out of the required keys dict as there are in it
result1 = sum(all(y in x for y in required_keys) for x in data)
print(f"part 1: {result1}")

# given a regex match and the limits in a list of two-element tuples, return if the limits match the integer in the string in the groups if not None
valid_ranges = lambda m, l: m is not None and not any(g is not None and (int(g) < l[i][0] or int(g) > l[i][1]) for i, g in enumerate(m.groups()))

# counts all entries like in the first part, but additionally check if the validation rules are matched with help of the defined lambda
result2 = sum(all(y in x and valid_ranges(re.match(r[0], x[y]), r[1:]) for y, r in required_keys.items()) for x in data)
print(f"part 2: {result2}")