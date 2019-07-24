class Stack:

    def __init__(self):
        self.stack = []

    def len_(self):
        """Checks length of the stack.
        
        Returns:
            int: number of items in the stack.

        Time: 
            Linear time:O(n).    
        """
        return len(self.stack)

    def is_empty(self):
        """Checks if stack has items.
        
        Returns:
            Bool: True if it is empty else False.

        Time:
            Constant time: O(1).     
        """

        if self.len_ == 0:
            return True
        else:
            return False

    def push(self, item):
        """Add item to stack.
        
        Args:
            item (iterable or int or float): Item to add on top of the stack.
        
        Raises:
            Exception: Cant add an item that is already in stack.

        Time:
            Constant time: O(1).    
        """
        if item not in self.stack:
            self.stack.append(item)
        else:
            raise Exception("Item already in stack")

    def pop(self):
        """Remove the last item to be added to the stack.
        
        Raises:
            Exception: If item is empty raise an exception.
        
        Returns:
             The item that was poped out.

        Time:
            constant time: O(1)     
        """
        if self.is_empty():
            raise Exception("No element in the Stack")
        else:
            return self.stack.pop()

    def peek(self):
        """Check the item that is on top of the stack.
        
        Returns:
            The item that was last added to the stack.
        """
        return self.stack[-1]
