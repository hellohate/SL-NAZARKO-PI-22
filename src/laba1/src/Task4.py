def count_expression(n: int = 18) -> float:
    a, b = 7, 2
    x = a * (a - 2*b) ** 2
    y = (2 * a + 3 * n) * a
    if x % 5 == 0:
        counted_sum = x / y
    else:
        counted_sum = y // x

    print(counted_sum)
    return counted_sum
