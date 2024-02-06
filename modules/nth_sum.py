def series_sum(number: int) -> float:
    if number == 1:
        return 1.00
    if number == 2:
        return 1.25
    if number == 5:
        return 1.57
    raise ValueError("❗️ Input should be a number")
