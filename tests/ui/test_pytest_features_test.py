import pytest
import random

@pytest.mark.regression
@pytest.mark.P1
def example():
    assert random.choice([True, True])
#
#
#