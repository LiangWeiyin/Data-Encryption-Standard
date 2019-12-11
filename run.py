import des

if __name__ == '__main__':
    mes = "Hello World! Life is short, you need python. Implement DES algorithm with python."
    key1 = list('1111101110111011101110111011101110111011101110111011101110111011')
    ciphertext = des.encryption(mes, key1)
    print(len(key1))
    print('密文: {}'.format(ciphertext))
    key2 = list('1111101110111011101110111011101110111011101110111011101110111011')
    plaintext = des.decryption(ciphertext, key2)
    print('明文: {}'.format(plaintext))
