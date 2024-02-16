from typing import List, Dict

def get_global_average(items: List[Dict[str, float]]):
    """Accepts a list of dicts of the following shape {average: float, count: int} and returns the weighted global average of the data."""
    if not items:
        return 0  # Return 0 or suitable default if items list is empty

    weighted_sum = sum(item["average"] * item["count"] for item in items)
    total_count = sum(item["count"] for item in items)

    if total_count == 0:
        return 0  # Avoid division by zero

    global_average = weighted_sum / total_count
    return global_average
