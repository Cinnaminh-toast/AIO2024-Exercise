def count_characters(word):
  output_dict = {}
  for character in word:
    output_dict[character] = output_dict.get(character, 0) + 1
  return output_dict
