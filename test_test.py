"""An example of test module in pytest."""
from test import total

def test_total_empty() -> None:
    """Total of an empty list should be 0.0."""
    assert total([]) == 0.0

def test_total_single_item() -> None:
    """Total of a single item list should be the first item's value."""
    assert total([28.16]) == 28.16

def test_total_many_items() -> None:
    """Total of a list with many"""
