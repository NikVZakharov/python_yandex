def partial_sums(*args):
    result = [0]
    total = 0
    for num in args:
        total += num
        result.append(total)
    return result
