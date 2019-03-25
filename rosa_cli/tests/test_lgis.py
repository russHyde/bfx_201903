from hypothesis import given, strategies as st

from rosa_cli import longest_increasing_subsequence,\
  longest_decreasing_subsequence

# ---- Unit tests

def test_it_isnt_greedy():
    assert longest_increasing_subsequence([1, 4, 2, 3, 5]) != [1, 4, 5]
    assert longest_decreasing_subsequence([1, 4, 2, 3, 5]) != [1]

def test_increasing_sequence():
    assert longest_increasing_subsequence([1, 3, 4, 2, 5, 7, 4]) == [1, 3, 4, 5, 7]

def test_decreasing_sequence():
    assert longest_decreasing_subsequence([4, 7, 5, 2, 4, 3, 1]) == [7, 5, 4, 3, 1]

def test_empty_sequence():
    assert longest_increasing_subsequence([]) == []

# ---- Randomised tests

@given(
    my_ints=st.lists(
        st.integers(min_value=1),
        max_size=1)
    )
def test_trivial_sequences(my_ints):
    assert my_ints == longest_increasing_subsequence(my_ints)

@given(
    my_ints=st.lists(
        st.integers(min_value=1),
        min_size=2,
        max_size=5,
        unique=True
    )
)
def test_with_sorted_unique_input(my_ints):
    assert sorted(my_ints) == longest_increasing_subsequence(sorted(my_ints))
