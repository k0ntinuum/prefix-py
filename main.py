import modes
from finds import *
# print(random_finds(
#     '|O@',
#     num_words = 8,
#     max_letters = 4
# ))
#finds = ['O','|','O|']
num_words = 5
print(
    str(
        modes.random_mode(
            finds = random_finds('O|@',num_words,4),
            alphabet = 'O|', 
            num_words = num_words, 
            num_letters = 7, 
            num_modes = num_words
)))