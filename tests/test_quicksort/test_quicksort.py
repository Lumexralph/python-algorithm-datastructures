from quicksort.quicksort import quicksort

class TestQuicksort:
    def test_that_sorting_arrays_succeeds(self):
      unsorted_array = [2, 1, 6, 3, 8, 4]

      sorted_array = quicksort(unsorted_array)

      assert sorted_array[0] == 1
      assert sorted_array[len(unsorted_array) - 1] == 8



