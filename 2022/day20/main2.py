decryption_key = 811589153

numbers = [decryption_key * int(line) for line in open("input.txt")]
new_indexes = list(range(len(numbers)))

for _ in range(10):
    for old_index, number in enumerate(numbers):
        number = number % (len(numbers) - 1)
        index = new_indexes.index(old_index)
        new_index = (index + number) % (len(numbers) - 1)
        if index < new_index:
            new_indexes[index:new_index] = new_indexes[index + 1 : new_index + 1]
            new_indexes[new_index] = old_index
        elif index > new_index:
            new_indexes[new_index + 1 : index + 1] = new_indexes[new_index:index]
            new_indexes[new_index] = old_index

new_numbers = [numbers[index] for index in new_indexes]
index = new_numbers.index(0)
print(
    sum(
        new_numbers[(index + offset) % len(new_numbers)]
        for offset in (1000, 2000, 3000)
    )
)
