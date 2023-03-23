import random
import string


def generate_password(lenght, letters=True, digits=False, symbols=False):
    password = ""
    if letters:
        password = string.ascii_letters
    if digits:
        password = password + string.digits
    if symbols:
        password = password + string.punctuation

    password = ''.join(random.choice(password) for i in range(lenght))

    return password


# def generate_password_letters_only(lenght: int):
#     letter = string.ascii_letters
#     password = ''.join(random.choice(letter)for i in range(lenght))
#
#     return password
#
#
# def generate_password_with_number(lenght: int):
#     letter = string.ascii_letters + string.digits
#     password = ''.join(random.choice(letter)for i in range(lenght))
#
#     return password
#
#
# def generate_password_with_special_char(lenght: int):
#     letter = string.ascii_letters + string.punctuation
#     password = ''.join(random.choice(letter) for i in range(lenght))
#
#     return password
#
#
# def generate_password_with_special_char_and_number(lenght: int):
#     letter = string.ascii_letters + string.punctuation + string.digits
#     password = ''.join(random.choice(letter) for i in range(lenght))
#
#     return password


if __name__ == '__main__':
    generate_password_letters_only(8)
