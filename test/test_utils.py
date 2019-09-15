import collections
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


# We use the `records` fixture here.

def test_transform(records):
    record = records[0]

    assert stakeholders.utils.transform(record) == {
        "monitor closely": {
            1: {
                "name": "stakeholder #1",
                1: {
                    "name": "deliverable #1"
                }
            }
        }
    }


def test_recursive_fold():
    left = {
        "monitor closely": {
            1: {
                "name": "stakeholder #1",
                1: {
                    "name": "deliverable #1"
                }
            }
        }
    }

    right = {
        "monitor closely": {
            1: {
                "name": "stakeholder #1",
                2: {
                    "name": "deliverable #2"
                }
            }
        }
    }

    assert stakeholders.utils.recursive_fold(left, right) == {
        "monitor closely": {
            1: {
                "name": "stakeholder #1",
                1: {
                    "name": "deliverable #1"
                },
                2: {
                    "name": "deliverable #2"
                }
            }
        }
    }


# We use the `records` fixture here.

def test_map_reduce(records):
    assert stakeholders.utils.map_reduce(records) == {
        "monitor closely": {
            1: {
                "name": "stakeholder #1",
                1: {
                    "name": "deliverable #1"
                },
                2: {
                    "name": "deliverable #2"
                }
            }
        },
        "keep satisfied": {
            2: {
                "name": "stakeholder #2",
                2: {
                    "name": "deliverable #2"
                }
            }
        },
        "keep informed": {
            3: {
                "name": "stakeholder #3",
                1: {
                    "name": "deliverable #1"
                }
            }
        },
        "monitor": {
            4: {
                "name": "stakeholder #4",
                1: {
                    "name": "deliverable #1"
                }
            }
        },
        "unknown": {
            5: {
                "name": "stakeholder #5",
                1: {
                    "name": "deliverable #1"
                }
            }
        }
    }


@pytest.mark.parametrize(
    ("unordered", "ordered"),
    [
        ({
            "unknown": {"key": "value"},
            "monitor": {"key": "value"},
            "keep informed": {"key": "value"},
            "keep satisfied": {"key": "value"},
            "monitor closely": {"key": "value"}
         },
            collections.OrderedDict({
                "monitor closely": {"key": "value"},
                "keep satisfied": {"key": "value"},
                "keep informed": {"key": "value"},
                "monitor": {"key": "value"},
                "unknown": {"key": "value"}
            })
        ),
        (
            {},
            collections.OrderedDict({
                "monitor closely": {},
                "keep satisfied": {},
                "keep informed": {},
                "monitor": {},
                "unknown": {}
            })
        )
    ]
)
def test_sort(unordered, ordered):
    assert stakeholders.utils.sort(unordered) == ordered
