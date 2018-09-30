from itertools import count, islice, takewhile, dropwhile
import functools
import math


def compose(*funcs):
    def compose2(f, g):
        def composed_func(*args):
            return g(f(*args))

        return composed_func

    first_func, *rest_funcs = funcs
    return functools.reduce(compose2, rest_funcs, first_func)


def fib(_=None):
    a = 1
    b = 1
    while True:
        yield b
        a, b = b, a + b


def primes(_=None):
    found_primes = set()
    found_primes.add(2)
    yield 2
    for i in count(3, 2):
        found_prime_factor = False
        for prime in found_primes:
            if i % prime == 0:
                found_prime_factor = True
                break
        if not found_prime_factor:
            found_primes.add(i)
            yield i


def primes_lte(limit):
    sieve = set()
    candidate = 2
    while True:
        for multiple in range(candidate * 2, limit + 1, candidate):
            sieve.add(multiple)
        found_new_prime = False
        for i in range(candidate + 1, limit + 1):
            if i not in sieve:
                found_new_prime = True
                yield i
                candidate = i
                break
        if not found_new_prime:
            break


def multiples_of(*divisors):
    def is_multiple(a, divisor):
        return a % divisor == 0

    def f(nums=None):
        if nums is None:
            nums = count()
        return filter(
            lambda a: any(is_multiple(a, divisor) for divisor in divisors), nums
        )

    return f


def lt(a):
    def f(nums=None):
        if nums is None:
            nums = count()
        return takewhile(lambda b: b < a, nums)

    return f


def gt(a):
    def f(nums=None):
        if nums is None:
            nums = count()
        return dropwhile(lambda b: b <= a, nums)

    return f


def even(nums=None):
    if nums is None:
        nums = count()
    return filter(lambda a: a % 2 == 0, nums)


def odd(nums=None):
    if nums is None:
        nums = count()
    return filter(lambda a: a % 2 == 1, nums)


def first(n=1):
    def f(nums=None):
        if nums is None:
            nums = count()
        return islice(nums, n)

    return f


def get_generator(seq):
    return seq()


def get_list(seq):
    return list(seq())


def get_first(seq):
    return next(seq())


def get_n(n, seq):
    return islice(seq(), n)


def get_sum(seq):
    return sum(seq())


def factors(a):
    for i in range(1, a + 1):
        if a % i == 0:
            yield i


def is_prime(a):
    return len(list(factors(a))) == 2


def prime_factors(a):
    square_root = math.floor(math.sqrt(a))
    for prime in primes_lte(square_root):
        if a % prime == 0:
            yield prime


# mults = multiples_of(3, 5)
# ltt = lt(200)
# seq = compose(mults, ltt)
# print(get_list(seq))
# seq = compose(mults, ltt, first(5))
# print(get_list(seq))

# seq = compose(mults, first(5), gt(100))
# print(get_list(seq))


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
    return


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
