import re
pattern = "\w+\.\w+\(.*?\)"
string = "base.all(j,hj)"
print(bool(re.match(pattern, string)))