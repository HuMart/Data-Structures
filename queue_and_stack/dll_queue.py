import sys
sys.path.append('../doubly_linked_list')
# from doubly_linked_list import DoublyLinkedList

class DoublyLinkedList:
    def __init__(self, node=None):
      self.head = node
      self.tail = node
      self.length = 1 if node is not None else 0

    def __len__(self):
      return self.length

class Queue:
  def __init__(self):
    self.size = 0
    # Why is our DLL a good choice to store our elements?
    self.storage = []

  def enqueue(self, value):
    self.storage.append(value)
    self.size += 1
  
  def dequeue(self):
    if self.size > 0:
      self.size -= 1
      return self.storage.pop(0)
    else:
      return None

  def len(self):
    return self.size
