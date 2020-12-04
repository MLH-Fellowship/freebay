import random
import string


ALPHANUMERIC_CHARS = string.ascii_lowercase + string.digits
STRING_LENGTH = 6

# function that generates a random string

def generate_random_string(
                            chars=ALPHANUMERIC_CHARS, 
                            length=STRING_LENGTH
                            ):
    return "".join(random.choice(chars) for _ in range(length))


# a function that generates unique slug for every 
# item posted on freebay

def generate_unique_slug(word):

    alphanumeric = ''

    for character in word:
        
        if character == " ":
            alphanumeric += "-"

        if character == "-":
            pass

        if character.isalnum():
            alphanumeric += character

    return alphanumeric +"-"+ generate_random_string()

