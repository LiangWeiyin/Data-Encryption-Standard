import des

if __name__ == '__main__':
    mes = "life"
    key = list('10011100111000111110000111101111110110011111001111100000011100011')
    ciphertext = des.encryption(mes, key)
    print('密文: {}'.format(ciphertext))
    plaintext = des.decryption(ciphertext, key)
    print('明文: {}'.format(plaintext))