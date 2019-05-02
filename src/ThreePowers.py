import itertools

import math

threepows = [3**i for i in range(41)]
s = itertools.combinations(threepows, 3)


# We know that floor(log_2(n+1)) indicates which numbers is located to the rightmost in the set.
g = math.ceil(math.log(9999999999999999+1)/math.log(2))
print(g)

# Lets find the 2^floor(log_2(n+1)) and 2^(floor(log_2(n+1))-1)
a = 2**(g-1)
b = 2**g

print(a, b)

# This does not yet work :9