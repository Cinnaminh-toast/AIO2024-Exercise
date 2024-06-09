# Calculate
# and print out f1 score with parameters
def calc_f1_score(tp, fp, fn):
  if not is_valid_input(tp, fp, fn):
    return

  precision = tp / (tp + fp)
  recall = tp / (tp + fn)
  f1_score = 2 * precision * recall / (precision + recall)
  
  print(f"""
    precision is {precision}\n
    recall is {recall}\n
    f1-score is {f1_score}
    """)

  return

# Check if input parameters are all valid
def is_valid_input(tp, fp, fn):
  if not isinstance(tp, int):
    print("tp must be int")
    return False

  if not isinstance(fp, int):
    print("tp must be int")
    return False

  if not isinstance(fn, int):
    print("tp must be int")
    return False

  if not (tp > 0 and fp > 0 and fn > 0):
    print("tp and fp and fn must be greater than zero")
    return False
  return True
