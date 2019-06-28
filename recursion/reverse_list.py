def reverse_list(S, left_index, right_index):
  if right_index != left_index:
    left_value, right_value = S[left_index], S[right_index]
    # swap them
    S[left_index], S[right_index] = right_value, left_value

    reverse_list(S, left_index + 1, right_index - 1)


S = [1, 2, 3, 4, 5, 6, 7]
reverse_list(S, 0, len(S) - 1)