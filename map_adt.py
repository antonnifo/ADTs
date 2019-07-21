class ChainMap:
    def __init__(self):
        """Python Maps also called ChainMap is a type of data structure to
           manage multiple dictionaries together as one unit.
           Implementation of a map using python list as the primary data storage.
        """
        self.dict = {}
        
    def create(self,*dict):
        """create a single dictionary from two dictionaries.
        
        Returns:
            dict: the created map
        """
        
        dicts = zip(*dict)
        for key,value in dicts:
            self.dict[key] = value
        return self.dict

    def update(self, key,value):
        """Add item to the map.
        
        Args:
            key (int or str): new key or the old key for the corresponding value.
            value (int or str): new value corresponding to the given key.
        """

        self.dict[key] = value
    
    def get_all_elements(self):
        """print all the key value of the map.
        """
        d = self.dict
        for key,value in d.items():
            print(key,value)

    def get_value(self,key_):
        """get a value that is corresponding to the given key.
        
        Args:
            key_ (str or int): key in the map to a corresponding value.
        
        Returns:
            int or str: a value of the corresponding key.
        """
        d = self.dict
        return d[key_]

    def get_len(self):
        """Return the length of the map.
        """
        return len(self.dict)


    def find_key(self, key):
        """perfome membership test on keys.
        
        Args:
            key: key value to test
        
        Returns:
            bool: if key is present it returns True else False
        """

        return key in self.dict        
