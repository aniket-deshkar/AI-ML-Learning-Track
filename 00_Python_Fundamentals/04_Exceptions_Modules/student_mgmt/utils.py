def average_marks(marks):
    if not marks:
        return None
    return round(sum(marks) / len(marks), 2)


def top_scorer(data):
    topper_name = " "
    topper_average = 0
    for value in data:
        average_value = average_marks(value["marks"])
        if average_value > topper_average:
            topper_name = value["name"]
            topper_average = average_value
    print(f"Top scorer: {topper_name},Average: {topper_average}")
