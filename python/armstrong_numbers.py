# How can you make this more scalable and reusable later?
def is_armstrong_number(number):
    if number < 10:
        return True
    digits = [int(num) for num in str(number)]
    power =len(digits)
    total = 0
    for digit in digits:
        total += digit ** power
    return total == number

def find_armstrong_numbers(numbers):
    armstrong_numbers = []
    for num in numbers:
        if is_armstrong_number(num):
            armstrong_numbers.append(num)
    return armstrong_numbers

