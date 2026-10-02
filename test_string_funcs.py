import string_funcs as sf

# unit test
def test_remove_vowels_happy_path():
    # 2 ways to check output in our test cases
    # 1. assert against a "desk calculation"
    result = sf.remove_vowels("gonzaga")
    assert result == "gnzg"

    # 2. assert against a known, validated implementation
    # e.g., a standard library
    # unsorted = [5,3,1,9]
    # our_sorted_list = sf.sort(unsorted)
    # python_sorted = unsorted.sorted()
    # assert our_sorted_list == python_sorted

def test_remove_vowels_empty_str():
    result = sf.remove_vowels("")
    assert result == ""

def test_remove_vowels_no_vowels():
    result = sf.remove_vowels("bcdfghjklmnpqrstvwxyz12~~!!")
    assert result == "bcdfghjklmnpqrstvwxyz12~~!!"

def test_remove_vowels_only_vowels():
    result = sf.remove_vowels("aAIioOeEUu")
    assert result == ""