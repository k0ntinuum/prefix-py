from finds import random_finds
from puts import random_puts
from goes import random_goes
from tg import *



def random_square_mode(alphabet, num_words, max_letters):
    assert num_words > len(alphabet)
    finds =  random_finds(alphabet, num_words, max_letters)
    assert  not finds == []
    puts = []
    while puts == []:
        puts = random_puts(alphabet,num_words, max_letters)
    goes = random_goes(num_words)
    m = []
    for i in range(num_words):
        m += [(finds[i], puts[i], goes[i])]
    return m

def random_square_key(alphabet, num_words, max_letters):
    k = []
    for i in range(num_words):
        k += [random_square_mode(alphabet, num_words, max_letters)]
    return k

def print_key(k):
    for i in range(len(k)):
        for j in range(len(k[i])):
            x = k[i][j]
            set_rgb(255,255,255)
            print(f"{i:3}{j:3}      ",end='')
            set_rgb(255,255,0)
            print(f"{x[0]:10s}",end='')
            set_rgb(255,0,0)
            print(f"{x[1]:10s}",end='')
            set_rgb(255,255,255)
            print(f"{x[2]:2d}",end='')
            print()
        print()

