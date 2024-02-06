def series_sum(number: int) -> float:
    if not isinstance(number, int):
        raise ValueError("❗️ Input should be a number")
    result = 0
    for value in range(1, number + 1):
        print(value)
        denominator = 1 if value == 1 else (value - 1) * 3 + 1
        result += 1 / denominator
    return round(result, 2)
