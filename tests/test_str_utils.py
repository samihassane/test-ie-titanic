# Filename has to start with test_
import pytest
from titanic_utils.str_utils import extract_titles

import hypothesis.strategies as st
from hypothesis import given


def test_dummy():
    # you can assert for whatever you want,
    # *but* peoply usally avoid them in production code
    # assert [1,2,3] == [1,2,3,4] to check for a mistake
    assert True


# @ = "Decorators"
@pytest.mark.parametrize(
    "expected_input, expected_output",
    [("Mr. John Doe", "Mr."), ("Miss. Jane Doe", "Miss."), ("Dr. Manhattan", "Dr.")],
)
def test_extract_titles_return_expected_output(expected_input, expected_output):
    # 2 Run the code
    output = extract_titles(expected_input)

    # 3 Verify
    assert output == expected_output


def test_extract_titles_without_dot_raises_error():
    with pytest.raises(ValueError):
        extract_titles("Alabama")


@given(st.text(alphabet=st.characters(blacklist_characters=["."])))
def test_extract_titles_with_gibberish_without_dots_raises_error(input_text):
    with pytest.raises(ValueError):
        extract_titles(input_text)
