def count_words(file_path):
  with open(file_path, "r") as f:
    data = f.read()
  
  data = data.lower()
  data = data.replace("\n", " ")
  word_list = data.split()
  output_dict = {}

  for word in word_list:
    output_dict[word] = output_dict.get(word, 0) + 1

  return output_dict
