# Calculate factorial
def factorial(n):
  result = 1
  for i in range(1, n + 1):
    result = result * i
  return result

# Approximate sine
def approx_sin(x, n):
  result = 0
  for i in range(n + 1):
    result = result + ((-1) ** i) * (x ** (2 * i + 1)) / factorial(2 * i + 1)
  return result

# Approximate cosine
def approx_cos(x, n):
  result = 0
  for i in range(n + 1):
    result = result + ((-1) ** i) * (x ** (2 * i)) / factorial(2 * i)
  return result

# Approximate sinh
def approx_sinh(x, n):
  result = 0
  for i in range(n + 1):
    result = result + (x ** (2 * i + 1)) / factorial(2 * i + 1)
  return result

# Approximate cosh
def approx_cosh(x, n):
  result = 0
  for i in range(n + 1):
    result = result + (x ** (2 * i)) / factorial(2 * i)
  return result
