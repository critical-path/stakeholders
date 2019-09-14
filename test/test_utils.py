import pytest
import stakeholders.utils


@pytest.mark.parametrize(
    ("power", "interest", "approach"), 
    [
        ("high", "high", "monitor closely"),
        ("high", "low",  "keep satisfied"),
        ("low", "high", "keep informed"),
        ("low", "low", "monitor"),
        ("invalid", "invalid", "unknown")
    ]
)
def test_compute_approach(power, interest, approach):
    assert stakeholders.utils.compute_approach(power, interest) == approach
