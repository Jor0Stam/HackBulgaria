from passlib.hash import pbkdf2_sha256

# pbkdf2_sha256.verify("password", hash) - verify passwords


def encrypt():
    def accepter(f):
        hash = pbkdf2_sha256.encrypt(f(), rounds=200000, salt_size=16)
        return hash
    return accepter


@encrypt()
def test(password=None):
    return password


def main():
    # a = pbkdf2_sha256.encrypt("a", rounds=200000, salt_size=16)
    # print(pbkdf2_sha256.verify("a", a))
    print(test("a"))


if __name__ == "__main__":
    main()
