import re

s = input()

print(re.sub(r"\D", "", s))
