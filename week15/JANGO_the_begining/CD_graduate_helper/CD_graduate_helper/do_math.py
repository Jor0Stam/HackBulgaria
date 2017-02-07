def get_factoriel(n):
    if n == 1:
        return 1
    else:
        return n * get_factoriel(n - 1)


def get_fibonaci(n):
    fnumbers = [1, 1]
    if n < 3:
        return 1
    else:
        for i in range(2, n):
            fnumbers.append(fnumbers[i - 1] + fnumbers[i - 2])
        return fnumbers[n - 1]


def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


def get_n_primes(n):
    primes = []
    if n == 1:
        return 1
    i = 2
    while n:
        if is_prime(i):
            n -= 1
            primes.append(i)
        i += 1
    return primes


def main():
    pass


if __name__ == "__main__":
    main()