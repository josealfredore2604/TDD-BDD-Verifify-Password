from app import verify_password

def test_strong_password():
    assert verify_password("Secure123") == "Strong password"

def test_weak_password_short():
    assert verify_password("abc") == "Weak password"

def test_weak_password_no_uppercase():
    assert verify_password("password1") == "Weak password"

def test_weak_password_no_number():
    assert verify_password("Password") == "Weak password"

def test_empty_password():
    assert verify_password("") == "Password required"
