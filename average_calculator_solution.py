def calculate_average(numbers):
    if not numbers:  # Handle empty list case
        return 0
    return sum(numbers) / len(numbers)