def quicksort(array):
  """function to sort an array
  
  using recursion to perform the operation

  Args:
    array(list): the array to be sorted
  
  Returns:
    the sorted array in ascending order
  """

  # the base case/index
  # array with length 0 or 1 will be sorted
  if len(array) < 2:
    return array
  else:
    """there should be a pivot which will
    values will be compared to, quicksort works this way
    """
    pivot = array[0]

    # generate array of elements less than the pivot
    less = [i for i in array[1:] if i <= pivot]

    # generate array of elements greater than the pivot
    greater = [i for i in array[1:] if i > pivot]

    return  quicksort(less) + [pivot] + quicksort(greater)
