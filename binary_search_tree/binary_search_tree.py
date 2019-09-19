from dll_queue import Queue
from dll_stack import Stack

# Questions:
# Only ints? 
# Negative numbers?

# Observations
# >= goes right
# Need to traverse to delete
# When deleting, the smallest child becomes parent


class BinarySearchTree:
  def __init__(self, value): # We're just using value, so key is value
    self.value = value
    self.left = None
    self.right = None

  # * `insert` adds the input value to the binary search tree, adhering to the
  # rules of the ordering of elements in a binary search tree.
  # Need to traverse to find spot to insert
  def insert(self, value):
    if value >= self.value:
      #Go to the right side
      if  not self.right :
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)
    else:
      if value < self.value:
        if not self.left:
          self.left = BinarySearchTree(value)
        else:
          self.left.insert(value)

  # * `contains` searches the binary search tree for the input value, 
  # returning a boolean indicating whether the value exists in the tree or not.
  # Start from root and traverse the tree
  # We can stop at the first instance of a value
  # We know it's not found if we get to a node that doesn't have children
  def contains(self, target):
    if target == self.value:
      return True
       
    if target > self.value: #Go to the right side
      if not self.right:
        return False
      else:
        return self.right.contains(target)

    if target < self.value:
      if not self.left:
        return False
      else:
        return self.left.contains(target)

  # * `get_max` returns the maximum value in the binary search tree.
  def get_max(self):
    if not self:
      return None
    else:
      if not self.right:
        return self.value
      else:
        return self.right.get_max()

  # * `for_each` performs a traversal of _every_ node in the tree, executing
  # the passed-in callback function on each tree node value. There is a myriad of ways to
  # perform tree traversal; in this case any of them should work. 
  def for_each(self, cb):
    cb(self.value)
    if self.left:
      self.left.for_each(cb)
    if self.right:
      self.right.for_each(cb)


  # Print all the values in order from low to high
  # Hint:  Use a recursive, depth first traversal
  def in_order_dft(self, node):
    if node.left:
      self.in_order_dft(node.left)

    print(node.value)

    if node.right:
      self.in_order_dft(node.right)

  # Print the value of every node, starting with the given node,
  # in an iterative breadth first traversal
  def bft_print(self, node):
    q = Queue()
    q.enqueue(node)
    current_node = node
    while q.size > 0:
      current_node = q.dequeue()
      print(current_node.value)
      if current_node.left:
        q.enqueue(current_node.left)
      if current_node.right:
        q.enqueue(current_node.right)
  
  # Print the value of every node, starting with the given node,
  # in an iterative depth first traversal
  def dft_print(self, node):
    st = Stack()
    st.push(node)
    current_node = node
    while st.size > 0:
      current_node = st.pop()
      print(current_node.value)
      if current_node.left:
        st.push(current_node.left)
      if current_node.right:
        st.push(current_node.right)

  # STRETCH Goals -------------------------
  # Note: Research may be required

  # Print In-order recursive DFT
  def pre_order_dft(self, node):
    if node:
      print(node.value)
      self.pre_order_dft(node.left)
      self.pre_order_dft(node.right)

  # Print Post-order recursive DFT
  def post_order_dft(self, node):
    if node:
      self.post_order_dft(node.left)
      self.post_order_dft(node.right)
      print(node.value)

