import bcrypt


def hash_password(password: str) -> str:
    hashed = bcrypt.hashpw(
        password.encode('utf-8'),
        bcrypt.gensalt()
    )
    return hashed.decode('utf-8')

def verify_password(stored: str, password: str) -> bool:
    return bcrypt.checkpw(
        password.encode('utf-8'),
        stored.encode('utf-8')
    )