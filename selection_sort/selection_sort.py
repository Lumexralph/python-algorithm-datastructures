"""Selection sort is slower than than quicksort
   before you can sort, you need a function to find the
   smallest number in a list/array
"""

def find_smallest(arr):
  """Function to find the smallest number in an array

  Args:
    arr(list): The list/array to find the index

  Returns:
    smallest_index(int): The index of the smallest number
  """
  smallest = arr[0] # stores the smallest value
  smallest_index = 0 # stores the position of the smallest value

  for i in range(1, len(arr)):
    if arr[i] < smallest:
      smallest = arr[i]
      smallest_index = i

  return smallest_index

def find_largest(arr):
  """Function to find the largest number in an array
  Args:
    arr(list): The list/array to find the index

  Returns:
    largest_index(int): The index of the largest number
  """

  largest = arr[0] # stores the largest value
  largest_index = 0 # stores the position of the largest value

  for i in range(1, len(arr)):
    if arr[i] > largest:
      largest = arr[i]
      largest_index = i

  return largest_index

def selection_sort(arr, order=0):
  """Function to sort the array
  Args:
    arr(list): The list/array to find the index

  Returns:
    largest_index(int): The index of the largest number

  Raises:
    error if the value provided is not a list/array or order
    is not an integer
  """

  if not isinstance(arr, list) or not isinstance(order, int):
    return "Please provide a list to be sorted or an integer for ordering"

  sorted_arr = []
  operation = find_largest if order else find_smallest

  for i in range(0, len(arr)):
    value = operation(arr)

    # append the smallest value into the new
    # array and remove it from the array
    sorted_arr.append(arr.pop(value))

  # the sorted array from smallest to largest
  return sorted_arr

