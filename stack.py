from node import Node

class Stack:
  def __init__(self, name):
    self.limit = 1000
    self.size = 0
    self.top_item = None
    self.name = name
    
  
  def push(self, value):
    if self.has_space():
      item = Node(value)
      item.set_next_node(self.top_item)
      self.top_item = item
      self.size += 1
    else:
      print("There is no more space on the stack")
  
  def pop(self):
    if not self.is_empty():
      item_to_remove = self.top_item
      self.top_item = item_to_remove.get_next_node()
      self.size -= 1
      return item_to_remove.get_value()
    else:
      print("Stack is empty")
  
  def peek(self):
    if not self.is_empty():
      return self.top_item.get_value()
    else:
      print("Stack is empty")
  
  def has_space(self):
    return self.size < self.limit
  
  def is_empty(self):
    return self.size == 0

  def get_size(self):
    return self.size
      
  def get_name(self):
    return self.name
  
  def print_items(self):
    pointer = self.top_item
    print_list = []
    while(pointer):
      print_list.append(pointer.get_value())
      pointer = pointer.get_next_node()
    print_list.reverse()
    print("{0} Stack: {1}".format(self.get_name(), print_list))
      
