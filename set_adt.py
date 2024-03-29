
class Set:

    def __init__(self,*data):
        """Implementation of a set using python list as the primary data storage.
            Acts like a set constructor.
        """
        self.set = list(data)


    def add(self, element):
        """Add one item to a set.
        
        Args:
            element (str or float or int): a single item to add to a set
        
        Run Time:
            constant time : o(1).
        """

        self.set.append(element)
        
    def update(self,*elements):
        """Add multiple items to a set.
         
         Args:
            element (str or float or int): multiple  items to add to a set
        
        Run Time:
            constant time : o(1).
        """

        self.set + list(elements)
        
    def get_all(self):
        """Loop through the set, and print all the values.
        
        Returns:
            [list]: a list of all elements in the set.

        Run Time:
            linear time : o(n)
        """

        our_set = self.set
        new_set = []
        for element in our_set:
            new_set.append(element)
        return new_set    

    def get_len(self):
        """Determine how many items a set has.
        
        Returns:
            [int]: the number of item in the set.
        
        Run Time:
            linear time : o(n)
        """

        return len(self.set) 

    def remove_(self,element):
        """Remove an item in a set.
        
        Args:
            Element ([int or str]): the item you want removed.
        
        Raises:
            KeyError: element is not in the set.

        Run Time:
            Linear time : o(n).    
        """

        if element in self.set:
            self.set.remove(element)
        else :
            raise KeyError("Element not in set try again")    

    def discard(self, element):
        """Remove an item in a set.
           Does not raise an error if item is not in the set. 
        
        Args:
            element (str or float or int): item to remove in the set.
        
        Run Time:
            constant time : o(1).
        """

        self.set.remove(element)
                  
    def clear(self):
        """Empty the set.

        Run Time:
            constant time : o(1).
        """

        self.set.clear()

    def copy(self):
        """Make a copy of the set.
        
        Returns:
            [set]: A copy of the set.

        Run Time:
            constant time : o(1).    
        """

        return set(self.set)
        
    def union(self,set_):
        """a set containing the union of another set.
        
        Args:
            set_ (set): The other set you want to check for union.
        
        Returns:
            [list]: All items in set 1 and set 2 withiout duplication.

        Run Time:
            constant time : o(1).    
        """

        set_1 = self.set
        new_set = set_1 or list(set_)
        return new_set  

    def intersection(self,set_2):
        """Is the set of all objects that are members of both the sets 1 and 2.
        
        Args:
            set_2 (set): The other set you want to check for intersection.
        
        Returns:
            [list]: Of all members that are present in both sets.

        Run Time:
            Linear time : o(1).    
        """

        set_1 = self.set
        new_set = []
        for element in set_1:
            if element in set_2:
                new_set.append(element)
        return new_set
  
    def is_disjoint(self,set_2):
        """Checks whether two sets have a intersection or not.
        
        Args:
            set_2 (set): The other set you want to check for intersection.
        
        Returns:
            [bool]: If intersection exists return True else False.

        Run Time:
            Linear time : o(n)    
        """
        
        if self.intersection(set_2):
            return True
        else:
            return False              
