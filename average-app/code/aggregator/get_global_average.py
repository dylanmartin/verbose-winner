def get_global_average(items: list[dict]):
    "accepts a list of dicts of the following shape {average: float, count: int} and returns the average of the data."
    global_average = sum([item["average"] for item in items])/len(items)
    return global_average