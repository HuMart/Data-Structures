from doubly_linked_list import DoublyLinkedList



class Stack:
  def __init__(self):
    self.size = 0
    # Why is our DLL a good choice to store our elements?
    self.storage = DoublyLinkedList()

  def push(self, value):
    self.size += 1
    self.storage.add_to_head(value)
  
  def pop(self):
    if self.storage == 0:
      return
    else:
      self.size -= 1
      num = self.storage.remove_from_head()
      return num
    

  def len(self):
    return self.size
x = Stack()
print(x.len())
x.push(4)
print(x.len())
x.push(6)
print(x.len())
print(x.pop())
