from test_data_gen import TestDataGenerator


def test_basic():

    # Given
    input_string = 'abc'

    # When
    output = TestDataGenerator.create_id_from_string(input_string)

    # Then
    assert output > 0
    assert isinstance(output, int)
