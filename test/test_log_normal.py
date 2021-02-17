from src.test_data_gen import TestDataGenerator


def test_basic():

    # Given
    mean = 100

    # When
    output = TestDataGenerator.log_normal(mean)

    # Then
    assert output >= 0.0
    assert isinstance(output, float)
