import math

# Given
# check if input n is a valid number
def is_number (n):
  try :
    float ( n ) # Type - casting the string to ‘float ‘.
                # If string is not a valid ‘float ‘ ,
                # it ’ll raise ‘ValueError ‘ exception
  except ValueError :
    return False
  return True

# Check if input function is valid
def is_valid_input_function(input_func):
  if input_func in ["sigmoid", "relu", "elu"]:
    return True
  return False

# Calculate sigmoid
def calc_sig(x):
  return 1 / (1 + math.e ** (-x))

# Calculate relu
def calc_relu(x):
  if x <= 0:
    return 0
  return x

# Calculate elu with default alpha
def calc_elu(x, alpha = 0.01):
  if x <= 0:
    return alpha * (math.e**x -1)
  return x

# Calculate
# and print out activation function based on user input
def calc_activation_func():
  x = input("Input x = ")
  if not is_number(x):
    print("x must be a number")
    return

  x = float(x)

  input_fn = input("Input activation Function ( sigmoid | relu | elu ) : ")
  if not check_input_function(input_fn):
    print(f"{input_fn} is not supportted")
    return

  if input_fn == "sigmoid":
    result = calc_sig(x)
  elif input_fn == "relu":
    result = calc_relu(x)
  else:
    result = calc_elu(x, alpha = 0.01)

  print(f"{input_fn} : f ({x}) = {result}")