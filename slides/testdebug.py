





# Sort numbers in a list
def sort_numbers(numbers):
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

print(sort_numbers(numbers))

