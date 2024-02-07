def calculate_denominator(value):
    return (value * 3) + 1

def series_sum(number: int) -> str:
    if not isinstance(number, int):
        raise ValueError("❗️ Input should be a number")
    result = 0
    for value in range(number):
        result += 1 / calculate_denominator(value)
    return "{:.2f}".format(result)
