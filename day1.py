import time


def part_one(target, data):
    for first_number in data:
        if target - first_number in data:
            return first_number * (target - first_number)


def part_two(target, data):
    for first_number in data:
        for second_number in data:
            if target - first_number - second_number in data:
                return (
                    first_number
                    * second_number
                    * (target - first_number - second_number)
                )


with open("inputs/1.txt", "r") as input_file:
    input_data = input_file.read().split("\n")
    input_data = [int(item) for item in input_data]

print(part_one(2020, input_data))
print(part_two(2020, input_data))
