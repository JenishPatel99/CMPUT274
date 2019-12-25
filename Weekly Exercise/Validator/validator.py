# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Name = Jenish Patel
# Student ID: 1572027
# CMPUT 274, FALL 2019
# Weekly Assignment: Validator (Part 2)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from random import randint, shuffle


def validate(password):
    """ The function analyzes the input password and determines if it is
    "Secure", "Insecure" or "Invalid" based on the criteria given in the
    the assignment. """
    length = len(password)
    invalid_chars = [" ", "_", "-"]
    spec_chars = list("!#$%&'()*+,./:;<=>?@[]^`{|}~")

    # Checks for validitity of the password
    if length < 8:
        return "Invalid"
    else:
        for i in password:
            for j in invalid_chars:
                if i == j:
                    return "Invalid"

    # Checks for a letter in the string
    i = 0
    is_alpha = False
    while i < len(password) and is_alpha is False:
        if password[i].isalpha() is True:
            is_alpha = True
        else:
            is_alpha = False
        i += 1

    # Checks for a lower case letter in the string
    i = 0
    is_lower = False
    while i < len(password) and is_lower is False:
        if password[i].islower() is True:
            is_lower = True
        else:
            is_lower = False
        i += 1

    # Checks for a upper case letter in the string
    i = 0
    is_upper = False
    while i < len(password) and is_upper is False:
        if password[i].isupper() is True:
            is_upper = True
        else:
            is_upper = False
        i += 1

    # Checks for an integer in the string
    i = 0
    is_numeric = False
    while i < len(password) and is_numeric is False:
        if password[i].isnumeric() is True:
            is_numeric = True
        else:
            is_numeric = False
        i += 1

    # If the first four conditions (above) are true,
    # it will check for a special character in the string
    spec_ch = False
    for i in password:
        for j in spec_chars:
            leave_loop = False
            while spec_ch is False and leave_loop is False:
                if i == j:
                    spec_ch = True
                else:
                    spec_ch = False
                    leave_loop = True

    if is_alpha and is_lower and is_upper and is_numeric and spec_ch is True:
        return "Secure"
    else:
        return "Insecure"

    pass


def generate(n):
    """ The generate function generate a string secure_password with
    length n which is guaranteed to be Secure by the given criteria
    in the assignment."""
    password_list = [''] * n
    spec_chars = list("!#$%&'()*+,./:;<=>?@[]^`{|}~")

    """ The first four elements of the list are a random set of special
    character, integers, upper case letters and lower case letter
    respectivily. The remaining elements are a random set of the four
    different types mention above. """
    for i in range(0, len(password_list)):
        if i < 4:
            if i == 0:
                password_list[i] = spec_chars[randint(0, 27)]
            if i == 1:
                password_list[i] = chr(randint(48, 57))
            if i == 2:
                password_list[i] = chr(randint(65, 90))
            if i == 3:
                password_list[i] = chr(randint(97, 122))
        else:
            password_list[i] = chr(randint(33, 122))

    # Rearranges the elements in the list for further unpredictablility.
    shuffle(password_list)

    # Joins the elements in password_list to create a string.
    secure_password = ''.join(password_list)

    """ If secure password contains invalid characters it will recurse the
    function again until a valid and secure password is generated. """
    message = validate(secure_password)
    while message == 'Invalid':
            secure_password = generate(n)
            message = validate(secure_password)

    return secure_password

    pass
