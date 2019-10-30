def filter_positive_even_nums(numbers):
    filtered = [num for num in numbers if num > 0 and num % 2 == 0]
    return filtered
