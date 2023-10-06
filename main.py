from demo import *
from key import *
from finds import *
from rect import *
alphabet = 'O|'
max_letters = 7
num_words = 5
num_modes = 5
#k = random_square_key(alphabet, num_words, max_letters)
k = random_rect_key(alphabet, num_words, num_modes, max_letters)
print_key(k)
demo_words(alphabet,k, 10, 10)