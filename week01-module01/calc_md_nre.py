# Calculate Difference of nth Root Error for single sample
def md_nre_single_sample(y, y_hat, n, p):
  return (y ** (1 / n) - y_hat ** (1 / n)) ** p
