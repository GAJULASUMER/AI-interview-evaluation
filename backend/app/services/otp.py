import random


def generate_otp() -> str:
    return "".join(str(random.randint(0, 9)) for _ in range(6))
