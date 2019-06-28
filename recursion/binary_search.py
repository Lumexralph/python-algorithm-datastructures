def binary_search(data, target, low, high):
    """Return True if target is found in indicated portion of a Python list
    Taking advantage of a sorted array or list
    """
    if low < 0 or high > len(data):
        return 'Please ensure low and high index are within range of the data'
    if low > high:
        return -1                # means we could not find the target
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            # recur on the portion left of the middle
            # interval is empty; no match
            # found a match
            return binary_search(data, target, low, mid - 1)
        else:
            # recur on the portion right of the middle
            return binary_search(data, target, mid + 1, high)


print(binary_search([1, 2, 3, 4, 5, 6], 1, 0, 6))