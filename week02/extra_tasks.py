# from fractions import Fraction


def simplify_fraction(fraction):
    temp_devisd = list(fraction)

    nom_devisers = find_prime_devisers(fraction[0])
    denom_devisers = find_prime_devisers(fraction[1])
    smaller = min(nom_devisers, denom_devisers)
    bigger = max(nom_devisers, denom_devisers)
    for i in range(len(smaller)):
        if smaller[i] in bigger:
            if temp_devisd[0] // smaller[i] < 1 or \
                    temp_devisd[1] // smaller[i] < 1:
                break
            temp_devisd[0] = temp_devisd[0] // smaller[i]
            temp_devisd[1] = temp_devisd[1] // smaller[i]

    if temp_devisd[0] == temp_devisd[1]:
        return 1
    else:
        return tuple(temp_devisd)


def find_prime_devisers(n):
    prime_devisers = [1]
    if prime_number(n):
        return [1, n]
    for i in range(2, int(n) // 2 + 1):
        if n % i == 0:
            prime_devisers.append(i)
    prime_devisers.append(n)

    return prime_devisers


def prime_number(number):
    status = True
    if number == 4:
        return False
    for i in range(2, int(abs(number)) // 2):
        if number % i == 0:
            status = False

    return status


def sort_fractions(fractions):
    for i in range(len(fractions) - 1):
        for j in range(len(fractions) - 1):
            temp = compare_fractions(fractions[j], fractions[j + 1])
            if temp != fractions[j]:
                fractions[j + 1] = fractions[j]
                fractions[j] = temp

    fractions.reverse()
    return fractions


def compare_fractions(frac1, frac2):
    # frac1 = simplify_fraction(frac1)
    # frac2 = simplify_fraction(frac2)

    if frac1[0] * frac2[1] > frac2[0] * frac1[1]:
        return frac1
    else:
        return frac2


def main():
    # print(simplify_fraction((4, 8)))
    print(sort_fractions([(22, 78), (15, 32), (5, 6),
                          (7, 8), (9, 6), (22, 7)]))


if __name__ == "__main__":
    main()
