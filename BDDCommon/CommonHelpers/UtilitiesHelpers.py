import random as rd
import string


def generate_random_user_and_password(
    domain: str = None, email_prefix: str = None
) -> dict:
    if not domain:
        domain = "example.com"

    if not email_prefix:
        email_prefix = "exmp"

    # Generate random email
    random_email_str_length = 10
    random_str = "".join(rd.choices(string.ascii_lowercase, k=random_email_str_length))

    email = f"{email_prefix}_{random_str}@{domain}"

    # Generate random password
    password_length = 20
    password_string = "".join(rd.choices(string.ascii_letters, k=password_length))

    kwargs = {"email": email, "password": password_string}

    return kwargs


def generate_random_name_and_last_name(
    f_name: str = "test_f", l_name: str = "test_f"
) -> dict:
    # Generate random name
    random_name_length = 5
    rd_name = "".join(rd.choices(string.ascii_lowercase, k=random_name_length))

    # Generate random last_name
    random_lastname_length = 8
    rd_last_name = "".join(rd.choices(string.ascii_lowercase, k=random_lastname_length))

    name = f"{f_name}_{rd_name}"
    last_name = f"{l_name}_{rd_last_name}"

    ## Create kwargs info
    kwargs = {"first_name": name, "last_name": last_name}

    return kwargs


def generate_random_coupon_code(
    code_prefix: str = "test", code_suffix: str = "test", rd_code_length: int = 5
) -> str:
    # Generate random code
    rd_code = "".join(rd.choices(string.ascii_lowercase, k=rd_code_length))

    code = f"{code_prefix}_{rd_code}_{code_suffix}"

    ## Create kwargs info
    return code
