
from pprint import pprint as pp

class TwoDmArray():
    """2DM array implementation using a Python list as underlying storage."""
    def __init__(self):
      """create an empty array."""  
      self.array    = []
    
    def create(self,data):
        '''Create a two-dm array.
        
        Args:
            data (sequence,float,int): elements to add to the two dm array.

        Run Time:
            constant time : o(1)    
        '''
        self.array.append(list(data))

    def get_array(self):
        '''Print all the elements in the 2-dm array.

        Run Time:
            Linear time : o(n)
        '''
        for row in self.array:
            for element in row:
                print(element, end=" ")
            print()    

    def get_num_rows(self):
        '''Count the number of rows.        
        
        Returns:
            int : number of rows of the 2dm array.

        Run Time:
            linear time : o(n)    
        '''
        
        return len(self.array)    

    def get_num_columns(self):
        '''Count the number of columns.        
        
        Returns:
            int : number of columns of the 2dm array.

        Run Time:
            linear time : o(n)    
        '''

        return len(self.array[0])         

    def del_element(self,row_index,column_index):
        '''Remove an element in the 2dm array.
        
        Args:
            row_index (int): row index of the element to be deleted.
            column_index (int): column index of the element to be removed.
        
        Raises:
            Exception: raise one if one of the index is not in the array.
        
        Returns:
            array: 2DM array.

        Run Time:
            constant time : o(1)    
        '''
        element = self.get_element(row_index, column_index)
        
        if element:
            del self.array[row_index][column_index]
            return self.get_array()

        raise Exception('index out of range')    

    def clear_array(self):
        '''Remove all items on the array withiout deleting the array.
        
        Run Time:
            constant time : o(1).
        '''

        self.array.clear()

    def get_element(self,row_index,column_index):
        '''Get a specific element from the array.
        
        Args:
            row_index (int): row index of the item in the array.    
            column_index (int): column index of the element in the array.
        
        Raises:
            Exception: raise one if index is out of range.
        
        Returns:
            the indexed element.

        Run Time:
            constant time : o(1)    
        '''

        element = self.array[row_index][column_index]
        if element:
            return element
        raise Exception('index out of range')    
        
    def update_element(self,row_index,column_index,item_value):
        '''Change the value of the indexed element.
        
        Args:
            row_index (int): row index reference of the item.
            column_index (int): column index reference of the item.
            item_value : the item to update the old one.
        
        Raises:
            Exception: raise one if the index is out of range.
        
        Returns:
            array: the 2dm array with the updated item.
        
        Run Time:
            constant time : o(1)
        '''

        element = self.get_element(row_index, column_index)
        if element:
            self.array[row_index][column_index] = item_value
            return self.get_array()
        raise Exception('index out of range')
