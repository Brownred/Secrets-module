import secrets
import string

characters_all = string.ascii_letters + string.digits + string.punctuation
password = secrets.choice(string.ascii_lowercase)
password += secrets.choice(string.ascii_uppercase)
password += secrets.choice(string.digits)
password += secrets.choice(string.punctuation)

for i in range(6):
    password += secrets.choice(characters_all)
    
pass_list = list(password)
secrets.SystemRandom().shuffle(pass_list)
password = "".join(pass_list)

print(f"secure password is {password}")
# Output oKrKG.C9'9

#Hard-to-guess password reset link
secureURL = "https://demo.com/user/pete/reset="
secureURL += secrets.token_urlsafe(32)

print(f"Secure URL is {secureURL}")
# Output https://demo.com/user/pete/reset=UzXVKJAwIv0SJpN9deU0iMlnoGyYyKq6ZWsEvLII7PY
