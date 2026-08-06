def calculate_stats(numbers):
    total_sum = sum(numbers)
    average = total_sum / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    return total_sum, average, maximum, minimum

numbers = [5,10,15,20,25]
total, avg, max_mum, min_mum = calculate_stats(numbers)

print(f"Total sum: {total}")
print(f"Averge: {avg}")
print(f"Maximum: {max_mum}")
print(f"Minimum: {min_mum}")