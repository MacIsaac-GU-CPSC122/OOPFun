def remove_vowels(phrase: str) -> str:
    new_str = ""
    for char in phrase.lower():
        if char not in "aeiou":
            new_str += char
    return new_str


def main():
    print(remove_vowels("gonzaga"))

if __name__ == "__main__":
    main()


    # a unit test is a function that tests another function for correctness
    # a unit test is comprised of one or more test cases
    # test cases should include simple/common input/output pairs (e.g., "happy path")
    # test cases should included complex/rare input/output pairs (e.g., edge cases)
    # test cases are built using assert statements
    # assert (AKA check) a statement is true
    # if the statement is true, execution continues as normal
    # if the statement is false, execution stops (crashes program with AssertionError)
    # example
    assert 3 == 4
    print("after assert")

    # we are going to use the pytest testing framework
    # test modules and unit tests start with test_
