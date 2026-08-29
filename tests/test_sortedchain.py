from collectionbox import SortedChain


def test_sorted_chain_keeps_values_ordered_across_blocks():
    chain = SortedChain(5)
    assert chain.index(5) == 1
    assert chain.lower_bound(5) == 1
    for value in [3, 7, 1, 9, 5, 4, 8, 2, 6, 0]:
        chain.add(value)

    expected = [0, 1, 2, 3, 4, 5, 5, 6, 7, 8, 9]
    assert list(chain) == expected
    assert list(reversed(chain)) == list(reversed(expected))
    assert [chain[index] for index in range(1, len(chain) + 1)] == expected
    assert repr(chain) == "SortedChain([0, 1, 2, 3, 4, 5, 5, 6, 7, 8, 9])"


def test_sorted_chain_searches_duplicates_and_bounds():
    chain = SortedChain(3)
    for value in [1, 3, 5, 3, 7, 3]:
        chain.add(value)

    assert 3 in chain
    assert 4 not in chain
    assert chain.find(3).value == 3
    assert chain.find(4) is None
    assert chain.index(3) == 2
    assert chain.index(4) == -1
    assert chain.lower_bound(3) == 2
    assert chain.upper_bound(3) == 6
    assert chain.lower_bound(9) == len(chain) + 1
    assert chain.upper_bound(9) == len(chain) + 1


def test_sorted_chain_removes_values_and_handles_empty_chain():
    chain = SortedChain(2)
    for value in [1, 2, 3, 2]:
        chain.add(value)

    chain.remove(2)
    assert list(chain) == [1, 2, 2, 3]
    chain.remove_all(2)
    assert list(chain) == [1, 3]
    assert chain.first() == 1
    assert chain.last() == 3

    chain.remove(1)
    chain.remove(3)
    assert not chain
    assert chain.first() is None
    assert chain.last() is None
    try:
        chain[0]
    except IndexError:
        pass
    else:
        raise AssertionError("expected indexing an empty chain to raise IndexError")

    chain.add(4)
    assert list(chain) == [4]
    chain.clear()
    assert len(chain) == 0
