import re

def is_valid_username(username):
    return bool(re.fullmatch(r"[A-Za-z0-9_]+", username))

def is_valid_password(password):
    return bool(re.fullmatch(r"(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])[A-Za-z0-9]+", password))

ALLOWED_DOMAINS = ["gmail.com", "outlook.com", "yahoo.com", "icloud.com", "hotmail.com", "kkumail.com"]

def is_valid_email(email):
    domain_pattern = "|".join(re.escape(domain) for domain in ALLOWED_DOMAINS)
    email_pattern = rf"^[A-Za-z0-9._%+-]{{6,30}}@({domain_pattern})$"
    return bool(re.fullmatch(email_pattern, email))
