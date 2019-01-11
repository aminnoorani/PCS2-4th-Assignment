def fibonacci(n, k):
  # Initial conditions
  if n == 1:
    return 1
  if n < 1:
    return 0
  else:
  # Recursive part
    return ((fibonacci(n - 2, k) * k) + fibonacci(n - 1, k))

print(fibonacci(29, 5))
