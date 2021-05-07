x = 7
y = 8
z = 0

result1 = x == y
result2 = y > x
result3 = z < x + 2
result4 = z - 1 < x + 2  # is the same as result4 = (z - 1) < (x + 2)

"""
ORDER OF OPERATIONS FOR CONDITIONALS
and
not
or
"""

result5 = result1 or result2 or result3
print(result5)

"""
The 'not' command reverses the boolean result

print(not (false and true)) = True
print(not (false or true)) = False
