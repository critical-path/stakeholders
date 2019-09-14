"""
This module contains utils.
"""


import collections
import functools


def compute_approach(power, interest):
    """
    Computes the approach to managing a 
    stakeholder according to the power/interest model.

    Parameters
    ----------
    power : str
        The stakeholder's level of power, either 
        `high` or `low`.

    interest : str
        The stakeholder's level of interest, either 
        `high` or `low`.

    Returns
    -------
    str
        The approach to managing this stakeholder:
        `monitor closely`, `keep satisfied`,
        `keep informed`, `monitor`, or `unknown`.
    """

    if power == "high" and interest == "high":
        return "monitor closely"
    elif power == "high" and interest == "low":
        return "keep satisfied"
    elif power == "low" and interest == "high":
        return "keep informed"
    elif power == "low" and interest == "low":
        return "monitor"
    else:
        return "unknown"


def transform(record):
    """
    Transforms (maps) a record.

    Parameters
    ----------
    record : dict
        The record to transform.

    Returns
    -------
    dict
        The transformed record.
    """

    return {
        record["stakeholder_approach"]: {
            record["stakeholder_id"]: {
                "name": record["stakeholder_name"],
                record["deliverable_id"]: {
                    "name": record["deliverable_name"]
                }
            }
        }
    }


def recursive_fold(left, right):
    """
    Recursively folds (reduces) two records.

    Parameters
    ----------
    left : dict
       The "left-hand", or current, record.

    right : dict
       The "right-hand", or next, record.

    Returns
    -------
    left : dict
        The folded (reduced) record.
    """

    # Iterate over each "level" of the record,
    # starting at approach, proceeding to stakeholder id, 
    # and then stopping at deliverable id.

    for key in right.keys():

        # This is the base case (a deliverable's name).
        if key == "name":
            pass

        # This is the recursive case.
        else:
            if key in left:
                recursive_fold(left[key], right[key])
            else:
                left[key] = right[key]

    return left


def map_reduce(records):
    """
    Maps and reduces a list of records.

    Calls the `transform` and `recursive_fold`
    functions.

    Parameters
    ----------
    records : list of dicts
        The records to map and reduce.

    Returns
    -------
    dict
        The mapped and reduced records.
    """

    if records:
        return functools.reduce(recursive_fold, map(transform, records))
    else:
        return {}


def sort(records):
    """
    Sorts records by the approach to managing stakeholders.

    Parameters
    ----------
    records : dict
        The records to sort.

    Returns
    -------
    OrderedDict
        The sorted records.
    """

    return collections.OrderedDict({
        "monitor closely": records.get("monitor closely", {}),
        "keep satisfied": records.get("keep satisfied", {}),
        "keep informed": records.get("keep informed", {}),
        "monitor": records.get("monitor", {}),
        "unknown": records.get("unknown", {})
    })
