import pytest
from data_structures.hashtable import Hashtable


def test_exists():
    assert Hashtable

def test_create():
    ht = Hashtable()
    actual = ht.size
    expected = 1024
    assert actual == expected

def test_hash():
    """
    hash
    arguments: key
    Returns: index in collection for that key
    """
    ht = Hashtable()
    index = ht.hash("cat")
    assert 0 <= index < ht.size


def test_set_apple():
    ht = Hashtable()
    ht.set('fruit', 'apple')
    fruit_index = ht.hash('fruit')
    actual = ht.buckets[fruit_index]
    expected = ('fruit','apple')
    assert actual.head.value == expected

# @pytest.mark.skip("TODO")
def test_get_apple():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_collisions():
    ht = Hashtable()
    ht.set("cat", "Josie")
    ht.set("act", "A Contemporary Theater")
    ht.set("tac", "Taco Tuesday")
    assert ht.get("cat") == ("Josie")
    assert ht.get("act") == ("A Contemporary Theater")
    assert ht.get("tac") == ("Taco Tuesday")


def test_contains():
    ht = Hashtable()
    ht.set('fruit', 'apple')
    ht.contains('fruit')
    assert True


def test_keys():
    ht = Hashtable()
    ht.set
