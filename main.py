from seq import *


def p0001():
    seq = compose(multiples_of(3, 5), lt(1000))
    return get_sum(seq)


def p0002():
    seq = compose(fib, lt(4_000_000), even)
    return get_sum(seq)


def p0003():
    a = 600851475143 // 1
    # a = 13195
    largest_prime_factor = max(prime_factors(a))
    return largest_prime_factor


def p0004():
    def pals():
        for a in n_digit_numbers(3)():
            for b in n_digit_numbers(3)():
                product = a * b
                if is_palindrome(product):
                    yield product

    return max(pals())


def p0005():
    return


def p0006():
    return


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
    print(
        "Problem",
        i + 1,
        "  ",
        "https://projecteuler.net/problem={}".format(i + 1),
    )
    print("---------")
    print(solution)
    print()
