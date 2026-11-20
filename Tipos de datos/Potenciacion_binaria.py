def pot_exp(n: int, m: int):
    binary = bin(m)[2:]
    result  = 1

    for digit in binary:
        result *= result
        if digit == "1":
            result *= n
    return result
