def binary_search(array, item):
  """function to search for the value in a list

  Args:
    array(list): a sorted list of values
    item: the value to be searched for in the array

  Returns:
    the position of the item from the list or a not found
  """

  low = 0
  high = len(array) - 1

  """whenever a search is to be made the high and low are added and
    divided by 2 to get the mid-point and look for the value at that
    result in the array. If it is the value, return the position, if
    what is found is less than the item found, make the highest point
    high to be the result - 1 and if it's higher, make the low point the
    result + 1
  """
  while low <= high:

    mid_point = (low + high) // 2

    guess = array[mid_point] # make the guess

    if guess == item:
      return mid_point

    if guess > item:
      high = mid_point - 1

    else:
      low = mid_point + 1

  """at this point, the loop could get any match"""
  return 'item not found in the array'
