from homework3.task3 import Filter, make_filter

sample_data = [
     {
         "name": "Bill",
         "last_name": "Gilbert",
         "occupation": "was here",
         "type": "person",
     },
     {
         "is_dead": True,
         "kind": "parrot",
         "type": "bird",
         "name": "polly"
     }
]


def test_filter():
    positive_even = Filter(
        lambda a: a % 2 == 0, lambda a: a > 0, lambda a: isinstance(a, int)
    )
    assert positive_even.apply(range(100)) == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36,
                                               38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70,
                                               72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]


def test2_filter():
    positive_odd = Filter(
        lambda a: a % 2 == 1, lambda a: a > 0, lambda a: isinstance(a, int)
    )
    assert [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25,
            27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49,
            51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73,
            75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97,
            99] == positive_odd.apply(range(100))


def test_make_filter():
    assert make_filter(name="polly", type="bird").apply(sample_data) == \
           [{'is_dead': True, 'kind': 'parrot', 'type': 'bird', 'name': 'polly'}]
