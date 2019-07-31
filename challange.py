def sumArray(arr=[3, 5, -4, 8, 11, 1, -1, 6], target=10):
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


def triples(arr=[3, 5, -4, 8, 11, 1, -1, 6], target=0):
    '''find all the possible triplets in the array, that sum up
     to a given target sum.
    
    Args:
        arr (list, optional): an array of integers. Defaults to [3, 5, -4, 8, 11, 1, -1, 6].
        target (int, optional): an array of integers. Defaults to 0.
    
    Returns:
        a list of tuples with triplets that add to target.

    Run time:
        quadratic time : O(n square)    
    '''
    triples = []
    for num in arr:
        for num2 in arr:
            sum_of_any_two = num + num2
            last_num = target - sum_of_any_two

            if last_num in arr:
                triples.append((num, num2, last_num))
    return triples


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


def quadruplets(arr=[7, 6, 4, -1, 1, 2], target=16):
    '''find all the possible quadruplets in the array,
     that sum up to the target number.
   
    Args:
        arr (list, optional): an array of integers. Defaults to [7, 6, 4, -1, 1, 2].
        target (int, optional): target sum. Defaults to 16.
    
    Returns:
        a list quadruplets.

    Run time:
        cubic time = O(n*3)    
    '''

    quadruplets = []
    for i in range(len(arr)):
        num = arr[i]
        for index in range(i+1, len(arr)):
            num2 = arr[index]
            for j in range(i+2, len(arr)):
                num3 = arr[j]
                sum_of_any_three = num + num2 + num3
                last_num = target - sum_of_any_three

                if last_num in arr:
                    quadruplets.append((num, num2, num3, last_num))
    return quadruplets
