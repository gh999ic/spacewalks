import pytest
from eva_data_analysis import text_to_duration

def test_text_to_duration_float():
    assert text_to_duration("10:20") == pytest.approx(10.33333333)

def test_text_to_duration_integer():
    assert text_to_duration("10:00") == 10
