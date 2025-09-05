# Print Sum of N Natural Numbers
def sum(N):
  if N == 0:
    return 0
  return sum(N-1) + N

print(sum(5))