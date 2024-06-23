class Stack:
  def __init__(self, capacity):
    self.__capacity = capacity
    self.__stack = []
  
  def is_empty(self):
    return len(self.__stack) == 0

  def is_full(self):
    return len(self.__stack) == self.__capacity

  def push(self, value):
    if not self.is_full():
      self.__stack.append(value)

  def pop(self):
    if not self.is_empty():
      return self.__stack.pop()

  def top(self):
    if not self.is_empty():
      return self.__stack[-1]
