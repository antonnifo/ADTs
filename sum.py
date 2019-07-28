def sumArray(arr=[3, 5, -4, 8, 11, 1, -1, 6], target = 10):
    '''check if there are any two elements that sums up to a given target in an array.
    
    Args:
        arr (list, optional): a list of integers or floats. Defaults to [3, 5, -4, 8, 11, 1, -1, 6].
        target (int, optional): the desired target sum. Defaults to 10.
    
    Returns:
        a list of the two numbers otherwise none.

    Run time:
        linear time: O(n)
    '''
  
    index_map = {}

    for index in range(len(arr)):
        num = arr[index]
        other = target - num

        if other in index_map:
            return [other, arr[index]]

        index_map[num] = index
    return None
