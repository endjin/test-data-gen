from src.test_data_gen import TestDataGenerator


def test_basic():

    # Given
    choices = ['a', 'b', 'c', 'd']

    # When
    output = TestDataGenerator.choose_log(choices)

    # Then
    assert output in choices
    assert isinstance(output, str)
