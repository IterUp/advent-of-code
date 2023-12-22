numbers = [int(line) for line in open("input.txt")]
for number in numbers:
    count = numbers.count(number)
    if count != 1:
        print(count, number)
    assert numbers.count(number) == 1

total = sum(numbers)
new_numbers = numbers[:]
for number in numbers:
    index = new_numbers.index(number)
    pre_mod = index + number
    new_index = pre_mod%len(numbers) - (pre_mod < 0)
    if index < new_index:
        new_numbers[index:new_index] = new_numbers[index+1:new_index+1]
        new_numbers[new_index] = number
    elif index > new_index:
        new_numbers[new_index+1:index+1] = new_numbers[new_index:index]
        new_numbers[new_index] = number
    assert sum(new_numbers) == total
index = new_numbers.index(0)
print(sum(new_numbers[(index+offset)%len(new_numbers)] for offset in (1000, 2000, 3000)))
