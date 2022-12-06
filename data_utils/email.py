def get_domain(email_address: str) -> str:
    return email_address.lower().split('@')[-1]


assert get_domain('kiwi@gmail.com') == 'gmail.com'
assert get_domain('kiwi@icloud.com') == 'icloud.com'
