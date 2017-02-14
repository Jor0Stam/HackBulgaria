from passlib.hash import pbkdf2_sha256


def encrypt_pass(f):
    def wrapper(*args, **kwargs):
        kwargs['password'] = pbkdf2_sha256.hash(kwargs['password'])
        return kwargs
    return wrapper

# >>> # verifying the password
# >>> pbkdf2_sha256.verify("toomanysecrets", hash)
# True
# >>> pbkdf2_sha256.verify("joshua", hash)
# False
