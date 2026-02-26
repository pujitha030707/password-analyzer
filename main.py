password = input("Enter your password: ")
length = len(password)
has_upper = any(c.isupper() for c in password)
has_lower = any(c.islower() for c in password)
has_digit = any(c.isdigit() for c in password)
has_symbol = any(not c.isalnum() for c in password)
score = sum([has_upper, has_lower, has_digit, has_symbol])
if length >= 8 and score >= 3:
    print("Strong Password")
elif length >= 6 and score >= 2:
    print("Medium Password")
else:
    print("Weak Password")
