from passlib.hash import sha256_crypt

# Hash a password
hashed_password = sha256_crypt.hash("mypassword")

# Verify a password
if sha256_crypt.verify("mypassword", hashed_password):
    print("Password is correct!")
else:
    print("Password is incorrect!")
