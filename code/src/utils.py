"""Utility functions
"""

import os
import hashlib


salt = os.urandom(32)


def generate_pw_hash(password):
    """Generate a hash value from a clear text password.
    Use PKCS5_PBKDF2_HMAC_SHA256 hashing algorithm.

    Return the hash value appended by the salt
    """
    return hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt,
        100000
    ) + salt
