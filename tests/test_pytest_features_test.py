import pytest
import random

@pytest.mark.regression
@pytest.mark.P1
@pytest.mark.flaky(reruns=2, reruns_delay=2)
def test_example():
    assert random.choice([True, False])
#
#
#