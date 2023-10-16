from math import prod


def is_prime(number):
    for divider in range(2, int(number ** 0.5) + 1):
        if number % divider == 0:
            return False
    return True
def has_3_prime_dividers(number):
    dividers = []
    for divider in range(2, int(number ** 0.5) + 1):
        if number % divider == 0:
            if is_prime(divider):
                dividers.append(divider)
            if divider != (number // divider) and is_prime(number // divider):
                dividers.append(number // divider)
    if (len(dividers)  == 3) and (dividers[0] % 10) == (dividers[1] % 10) == (dividers[2] % 10) and prod(dividers) == number:
            return True
    return False
answers = []
for number in range(318216, 369454):
    if has_3_prime_dividers(number):
        answers.append(number)
print(len(answers), min(answers))
