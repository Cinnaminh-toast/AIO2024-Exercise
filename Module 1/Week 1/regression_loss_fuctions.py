import math
import random

# Calculate
# and print out loss by regression function from user input
def calc_loss_by_regression_fn():
  num_samples = input("""
    Input number of samples ( integer number ) which are generated :
    """)

  if not num_samples.isnumeric():
    print("number of samples must be an integer number")
    return

  input_fn = input("Input loss name : ")

  cummulative_loss = 0
  for i in range(int(num_samples)):
    target = random.random() * 10
    predict = random.random() * 10
    if input_fn == "MAE":
      loss_i = abs(target - predict)
    else:
      loss_i = (target - predict)**2

    cummulative_loss = cummulative_loss + loss_i
    to_print = f"""
      loss name : {input_fn},
      sample : {i},
      pred : {predict},
      target : {target},
      loss : {loss_i}
    """
    print(to_print)
  if input_fn == "RMSE":
    final_loss = math.sqrt((cummulative_loss / num_samples))
  else:
    final_loss = cummulative_loss / num_samples

  print(f"final {input_fn} : {final_loss}")
  return