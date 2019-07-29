def smallest_difference(A=[-1, 5, 10, 20, 28, 3], B=[26, 134, 135, 15, 17]):
    '''find the pair of numbers where one number comes from the first array,
     and another number comes from the second array with the smallest difference.

    
    Args:
        A (array, optional): array of integer values. Defaults to [-1, 5, 10, 20, 28, 3].
        B (array, optional): array of integer values. Defaults to [26, 134, 135, 15, 17].
    
    Returns:
        tuple: pair of ints with the smallest  difference.

    Run time:
            quasilinear time: O(n log n)     
    '''
  
    a = sorted(A)
    b = sorted(B)
    min_a = a[0]
    min_b = b[0]

    if min_a < min_b:
        
        return min_a, b[-1]

    elif min_a > min_b:
       
        return min_b, a[-1]

    elif min_a == min_b:

        if b[-1] > a[-1]:
            
            return a[0], b[-1]

        elif b[-1] < a[-1]:
            
            return a[0], a[-1]
