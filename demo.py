from encode import *
from decode import *
from words import *
from tg import *
import numpy as np




def nth_word(alphabet, n):
    l = len(alphabet)
    y = ''
    pattern = str(np.base_repr(n,l))
    for i in range(len(pattern)):
        y += alphabet[int(pattern[i])]
    return y







def demo_words(alphabet, k, n, max_letters):
    for i in range(n):
        #w = a_random_word(alphabet, 1, max_letters)
        w = nth_word(alphabet,i)
        e = square_encode(k,w)
        set_rgb(255,255,255)
        print(f"f {w:20s}",end='')
        set_rgb(255,255,0)
        print(f" {e:20s}")


