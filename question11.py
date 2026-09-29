numbers = [10, 15, 20, 25, 30]

def count_even(numbers):
    count = 0

    for number in numbers:
        if number % 2 == 0:
            count += 1
    return count

result = count_even(numbers)
print(result)