import words
import numpy as np
from words import a_random_word
from finds import *
from demo import *
from key import *

def random_rect_mode(alphabet, num_words, num_modes, max_letters):
    assert num_words > len(alphabet)
    finds =  random_finds(alphabet, num_words, max_letters)
    assert  not finds == []
    puts = []
    while puts == []:
        puts = random_puts(alphabet,num_words, max_letters)
    goes = random_goes(num_modes)
    m = []
    for i in range(num_words):
        m += [(finds[i], puts[i], goes[i])]
    return m

def random_rect_key(alphabet, num_words, num_modes, max_letters):
    k = []
    for i in range(num_modes):
        k += [random_rect_mode(alphabet, num_words, num_modes, max_letters)]
    return k