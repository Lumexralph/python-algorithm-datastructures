def count_items_in_list(items):
  """function to recursively count items in a list

  without using the len() function

  Args:
    items(list): an array of items

  Returns:
    int: the count of items in a list
  """
  if not isinstance(items, list):
    return "data not a list/array"

  try:
    # remove first item from the list
    # it reduces the size of the list
    # make a copy
    copy_of_items = items[:]

    copy_of_items.pop(0)

    return 1 + count_items_in_list(copy_of_items)

  except IndexError:
    # the base case or index when there's no
    # element left in the list, means it is empty
    return 0

