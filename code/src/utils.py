import os
import hashlib


salt = os.urandom(32)


def generate_pw_hash(password):
    return hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt,
        100000
    ) + salt
