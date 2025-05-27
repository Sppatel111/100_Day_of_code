# Email Validator
#
# Validates an email format using regex and functions.
import re
def validate_mail(e):
    pattern=r'^[^@]+@[^@]+\.[^@]+$'
    return re.match(pattern,e) is not None

print(validate_mail('abc@gmail.com'))