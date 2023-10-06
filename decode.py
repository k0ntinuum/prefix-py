def _square_decode(key, mode, ciphertext):
    for i in range(len(key)):
        finds = key[mode][i][0]
        puts = key[mode][i][1]
        if ciphertext.startswith(puts):
            return (finds, ciphertext[len(puts):],key[mode][i][2])
    raise ValueError('could not decode')
        
def square_decode(key, ciphertext):
    mode = 0
    plaintext = ''
    while not ciphertext == '':
        result = _square_decode(key, mode, ciphertext)
        plaintext += result[0]
        ciphertext = result[1]
        mode = result[2]
        print('c =', ciphertext, 'p =', plaintext, 'm = ',mode)
    return plaintext