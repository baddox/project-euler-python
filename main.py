from seq import *


def p0001():
    # 233168
    seq = compose(multiples_of(3, 5), lt(1000))
    return get_sum(seq)


def p0002():
    # 4613732
    seq = compose(fib, lt(4_000_000), even)
    return get_sum(seq)


def p0003():
    # 6857
    a = 600851475143
    largest_prime_factor = max(prime_factors(a))
    return largest_prime_factor


def p0004():
    # 906609
    def pals():
        for a in n_digit_numbers(3)():
            for b in n_digit_numbers(3)():
                product = a * b
                if is_palindrome(product):
                    yield product

    return max(pals())


def p0005():
    # 232792560
    return lcm(*range(1, 21))


def p0006():
    # 25164150
    nums = range(1, 101)
    sum_of_squares = sum(squares(nums))
    square_of_sum = sum(nums) ** 2
    return square_of_sum - sum_of_squares


def p0007():
    return


def p0008():
    return


def p0009():
    return


def p0010():
    return


problems = [
    p0001,
    p0002,
    p0003,
    p0004,
    p0005,
    p0006,
    p0007,
    p0008,
    p0009,
    # p0010,
]

print()
for i, problem in enumerate(problems):
    solution = problem()
    if solution is None:
        continue
    print("https://projecteuler.net/problem={}".format(i + 1), "=", solution)
