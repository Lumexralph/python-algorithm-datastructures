from recursive_count_items.recursive_count_items import count_items_in_list

class TestCountItemsInList:
    def test_that_the_item_counted_succeeds(self):

        my_list = [1, 2, 3, 4, 5]

        result = count_items_in_list(my_list)

        assert result == len(my_list)

    def test_that_counts_list_with_no_item(self):

        empty_list = []

        result = count_items_in_list(empty_list)

        assert result == 0

    def test_that_only_list_is_supplied(self):

        non_list = 'Game'

        result = count_items_in_list(non_list)

        assert result == 'data not a list/array'
