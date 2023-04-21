import requests
import hashlib

def check_password(password):
    # Create SHA1 hash of the password
    hashed_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

    # Split the hash into a prefix and suffix
    prefix, suffix = hashed_password[:5], hashed_password[5:]

    # Send a GET request to the HIBP API
    response = requests.get(f'https://api.pwnedpasswords.com/range/{prefix}')

    # Check if the suffix appears in the response
    for line in response.text.splitlines():
        line_prefix, count = line.split(':')
        if line_prefix == suffix:
            return int(count)

    # If the suffix doesn't appear in the response, the password is safe
    return 0

# Test the function with a sample password
password = 'password123'
count = check_password(password)

if count:
    print(f'The password "{password}" has been pwned {count} times. You should choose a different password.')
else:
    print(f'The password "{password}" has not been pwned. You can use it.')
