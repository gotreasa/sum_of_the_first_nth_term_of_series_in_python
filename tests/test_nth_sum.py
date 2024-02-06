import pytest
from modules import nth_sum


def describe_nth_sum():
    def should_error_if_not_number():
        """🧪 should return an error if the input is not a number"""
        with pytest.raises(ValueError, match="❗️ Input should be a number"):
            nth_sum.series_sum("blah")
