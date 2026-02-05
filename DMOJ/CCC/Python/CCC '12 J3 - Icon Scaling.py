
"""
*x*
 xx
* *
"""

k = int(input())

for i in range(k): print(('*' * k) + ('x' * k) + ('*' * k))
for i in range(k): print((' ' * k) + ('x' * k) + ('x' * k))
for i in range(k): print(('*' * k) + (' ' * k) + ('*' * k))
