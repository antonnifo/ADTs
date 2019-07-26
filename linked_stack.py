class LinkedListStack:
    """LIFO Stack implementation using a singly linked list 
    for storage."""
   
    # Nested node class

    class Node:
        """Lightweight, nonpublic class for storing a singly
         linked node."""

        def __init__(self,value,next_node):
            self.value     = value
            self.next_node = next_node

    def __init__(self):
        self.head = None
        self.size = 0

    def len(self):
        """Return the number of elements in the stack.
        
        Returns:
            int: count of items in the stack.

        Run Time:
            constant time : o(1)
        """
        return self.size

    def is_empty(self):
        """Check weather the stack has items.
        
        Returns:
            Boolean: True if the stack is empty otherwise False.

        Run Time:
                constant time : o(1)
        """
        return self.size == 0
    
    def push(self,value):
        """Add an item to the top of the stack.
        
        Args:
            value (int or str): Item to add on the stack.

        Run Time:
                constant time : o(1)
        """
        self.head = self.Node(value, self.head)
        self.size += 1

    def pop(self):
        """Remove and return the element from the top of the stack.
        
        Raises:
            Exception: Raises an exception if stack is empty.
        
        Returns:
            The item removed.

        Run Time:
                constant time : o(1)
        """

        if self.is_empty():
            raise Exception("Stack is empty")

        item_to_remove = self.head.value
        self.head = self.head.next_node
        self.size -= 1
        return item_to_remove

    def peek(self):
        """Get's the element at the top of the stack withiout removing it.
        
        Raises:
            Exception: Raise one if the stack is empty.
        
        Returns:
            Item at the top of the stack.

        Run Time:
                constant time : o(1)
        """
        
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.head.value
