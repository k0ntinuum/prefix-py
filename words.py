import random
import secrets
def a_random_word(alphabet, min_letters, max_letters):
    x = ''
    l = secrets.randbelow(max_letters - min_letters + 1) + min_letters
    for i in range(l):
        x += random.choice(alphabet)
    return x