import pytest

def search_item(nums, k):
    return k in nums

@pytest.mark.parametrize(
        "nums, k, expected", 
        [
            ([1, 2, 4], 1, True),
            ([1, 3, 3, 454], 44, False),
            ([], 4, False)
        ]
)
def test_search_item(nums, k, expected):
    assert search_item(nums, k) == expected 


def test_different_assert():
    assert 3 in [4, 3, 90, 2]
    assert 6 < 40
    assert 190 > 90
    assert 600 != 599.9
    assert "mango" not in "I love football"
    assert "what a day" in "what a day, i have learnt so much"
    x = "Entry level jobs are hard to come by"
    assert x != "Entry level jobs are hard to come by", "It was equal I lied"
