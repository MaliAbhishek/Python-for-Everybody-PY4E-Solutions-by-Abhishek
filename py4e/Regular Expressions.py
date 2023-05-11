import re
print(sum(map(int, re.findall('[0-9]+', open('regex_sum_1451876.txt').read()))))