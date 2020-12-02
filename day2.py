
def part_one(given_data):
    valid_passwords = 0
    for row in given_data:
        policy, password = row.split(':')
        policy = policy.strip()
        password = password.strip()
        lower_limit, rest_policy = policy.split('-')
        upper_limit,letter = rest_policy.split(' ')
        lower_limit = int(lower_limit)
        upper_limit = int(upper_limit)
        count_limit = list(range(lower_limit,upper_limit+1))
        letter = letter.strip()
        letter_count = password.count(letter)
        if letter_count in count_limit:
            valid_passwords += 1
    return valid_passwords

def part_two(given_data):
    valid_passwords = 0
    for row in given_data:
        policy, password = row.split(':')
        policy = policy.strip()
        password = password.strip()
        lower_limit, rest_policy = policy.split('-')
        upper_limit,letter = rest_policy.split(' ')
        #Account for no zero position
        lower_limit = int(lower_limit)-1
        upper_limit = int(upper_limit)-1
        if password[lower_limit] == letter and password[upper_limit] != letter:
            valid_passwords += 1
        elif password[lower_limit] != letter and password[upper_limit] == letter:
            valid_passwords += 1
        else:
            pass
    return valid_passwords

with open("inputs/2.txt", "r") as input_file:
    input_data = input_file.read().split("\n")
    input_data = [item for item in input_data]

print(part_one(input_data))
print(part_two(input_data))