import sys
from math import gcd

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    step, mod = map(int, line.split())
    if gcd(step, mod) == 1:
        result = "Good Choice"
    else:
        result = "Bad Choice"
    # UVA requires formatting and a blank line after each case
    print(f"{step:10d}{mod:10d} {result}")
    print()
