#Filename has to start with test_

def test_dummy():
    # you can assert for whatever you want,
    # *but* peoply usally avoid them in production code
    # assert [1,2,3] == [1,2,3,4] to check for a mistake
    assert True

from titanic_utils.str_utils import extract_titles


def test_extract_titles_return_expected_output():
    #1. Preconditions
    expected_input = "Mr. John Doe"
    expected_output = "Mr."

    #2 Run the code
    output = extract_titles(expected_input)

    #3 Verify
    assert output == expected_output