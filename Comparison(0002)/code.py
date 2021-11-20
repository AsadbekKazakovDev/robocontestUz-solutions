# Katta-kichik (Comparison)
# One of the most important tasks to do when working with numbers is comparison. In this proble, what you are required to do is compare two integers.
# Input:
# There will be 2 numbers submitted, A and B, whose absolute value is less than 2*(10**9).

# Output:
# The out put should be either ">" - A > B, "<" A < B, or "=" A = B.
a,b=map(int,input().split())
if a > b:
  print('>')
elif a < b:
  print('<')
else:
  print('=')
