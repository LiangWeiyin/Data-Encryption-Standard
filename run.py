import des

if __name__ == '__main__':
    mes = "Hello World!"
    key1 = list('1011101110111011101110111011101110111011101110111011101110111011')
    ciphertext = des.encryption(mes, key1)
    print('密文: {}'.format(ciphertext))
    key2 = list('1011101110111011101110111011101110111011101110111011101110111011')
    plaintext = des.decryption(ciphertext, key2)
    print('明文: {}'.format(plaintext))
    with open('ciphertext.txt', 'w+', encoding='utf-8') as f:
        f.write('{}\n'.format(ciphertext))
    with open('plaintext.txt', 'w+', encoding='utf-8') as f:
        f.write('{}\n'.format(plaintext))