def verify_password(password):
    if not password:
        return "Password required"
    if len(password) >= 8 and any(c.isupper() for c in password) and any(c.isdigit() for c in password):
        return "Strong password"
    return "Weak password"
