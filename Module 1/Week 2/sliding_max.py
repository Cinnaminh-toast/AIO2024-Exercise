def get_sliding_max(num_list, k):
  output = []
  for i in range(len(num_list) - k + 1):
    output.append(max(num_list[i:i+k]))
  return output
