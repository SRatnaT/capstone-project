import re

# Without DRY
# def validate_email_format_1(email: str) -> bool:

#     # Validation logic
#     if re.search(r'@', email) and re.search(r'\.', email):
#         return True
#     else:
#         return False


# def validate_email_format_2(email: str) -> bool:
#     # Validation logic
#     if re.search(r'@', email) and re.search(r'\.', email):
#         return True
#     else:
#         return False

# With DRY


def validate_email_format(email: str) -> bool:

    if re.search(r"@", email) and re.search(r"\.", email):
        return True
    else:
        return False


print(validate_email_format("sailratna1@gmail.com"))
