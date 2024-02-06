import pytest
from modules import nth_sum


def describe_nth_sum():
    def should_error_if_not_number():
        """🧪 should return an error if the input is not a number"""
        with pytest.raises(ValueError, match="❗️ Input should be a number"):
            nth_sum.series_sum("blah")
            
    def should_return_1_for_1():
        """🧪 should return 1.00 for the input 1"""
        assert nth_sum.series_sum(1) == 1.00
            
    def should_return_125_for_2():
        """🧪 should return 1.25 for the input 2"""
        assert nth_sum.series_sum(2) == 1.25
