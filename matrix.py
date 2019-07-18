# 2dm rows and columns where individual elemens can be a
from pprint import pprint as pp

class TwoDmArray():
    """2DM array implementation using a Python list as underlying storage."""
    def __init__(self):
      """create an empty array"""  
      self.array    = []
    
    def create(self,data):
        """accepts any sequence at a time as row"""   
        self.array.append(list(data))

    def get_array(self):
        """print out the entire two dimensional array """
        for row in self.array:
            for element in row:
                print(element, end=" ")
            print()    

    def get_num_rows(self):
        """returns the number of rows"""
        
        return len(self.array)    

    def get_num_columns(self):
        """return the number of columns"""

        return len(self.array[0])         

    def del_element(self,row_index,column_index):
        """Removes an element from the two dimensional array"""
        element = self.get_element(row_index, column_index)
        if element:
            del self.array[row_index][column_index]
            return self.get_array()
        raise Exception('index out of range')    

    def clear_array(self):
        """Removes all the elements from the two dimensional array"""

        self.array.clear()
        return self.array

    def get_element(self,row_index,column_index):
        """get a specific array from the matrix"""

        element = self.array[row_index][column_index]
        if element:
            return element
        raise Exception('index out of range')    
        
    def update_element(self,row_index,column_index,item_value):
        """update the value of an element in the matrix"""

        element = self.get_element(row_index, column_index)
        if element:
            self.array[row_index][column_index] = item_value
            return self.get_array()
        raise Exception('index out of range')
