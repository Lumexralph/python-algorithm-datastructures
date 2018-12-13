from selection_sort.selection_sort import selection_sort

class TestSelectionSort:
    def test_that_list_sorted_in_descending_succeeds(self):

        my_list = [1, 2, 3, 4, 5]

        sorted_list = selection_sort(my_list, 1)

        assert sorted_list[0] == 5

    def test_that_list_sorted_in_descending_fails(self):

        my_list = [1, 2, 3, 4, 5]

        sorted_list = selection_sort(my_list, '1')

        assert sorted_list == 'Please provide a list to be sorted or an integer for ordering'

    def test_that_list_sorted_in_ascending_succeeds(self):

        my_list = [9, 8, 7, 4, 3, 2, 0, 6, 5]

        sorted_list = selection_sort(my_list)

        assert sorted_list[0] == 0

    def test_that_list_sorted_in_ascending_fails(self):

        my_list = 9

        sorted_list = selection_sort(my_list)

        assert sorted_list == 'Please provide a list to be sorted or an integer for ordering'
