from random import shuffle

def bubble_sort(unsorted_iterable):
    list_obj = list(unsorted_iterable)
    is_ordered = False
    unsorted_len = len(list_obj)

    while not is_ordered:
        is_ordered = True

        unsorted_len -= 1
        for i in range(unsorted_len):
            if list_obj[i] > list_obj[i + 1]:
                list_obj[i], list_obj[i + 1] = list_obj[i + 1], list_obj[i]
                is_ordered = False

    return list_obj


def test_one_element():
    assert [1] == bubble_sort([1])


def test_already_ordered_list():
    ordered = range(10)
    assert ordered == bubble_sort(ordered)


def test_reversed_list():
    ordered = range(10)
    assert ordered == bubble_sort(ordered[::-1])


def test_shuffled_list():
    list_ = range(10)
    shuffle(list_)
    assert range(10) == bubble_sort(list_)


def test_sorts_other_iters():
    list_ = range(10)
    shuffle(list_)
    assert range(10) == bubble_sort(tuple(list_))
