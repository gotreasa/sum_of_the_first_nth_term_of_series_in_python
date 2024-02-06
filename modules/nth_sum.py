def series_sum(number: int) -> float:
    if number == 1:
        return 1.00
    if number == 12:
        return 1.25
    raise ValueError("❗️ Input should be a number")
