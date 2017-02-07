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
    for i in range(2, n // 2):
        if isinstance(n / i, int):
            return False
    return True


def get_nth_prime(n):
    if n == 1:
        return 1
    i = 2
    while n:
        if is_prime(i):
            n -= 1
        i += 1
    return i


def main():
    print("TEST")
    print(is_prime(5))


if __name__ == "__name__":
    main()
