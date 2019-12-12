import des

if __name__ == '__main__':
    mes = "testtesttesttesttesttesttesttesttesttest"
    key1 = list('1111101110111011101110111011101110111011101110111011101110111011')
    IV = list('0110001100000101100010101000100001000011110110010000010100110110')
    key2 = list('1111101110111011101110111011101110111011101110111011101110111011')

    ciphertext = des.encryption(mes, key1)
    # ciphertext = des.encryption(mes, key1, mod='CBC', iv=IV)
    with open('ciphertext.txt', 'w+', encoding='utf-8') as f:
        f.write('{}\n'.format(ciphertext))
    print('密文: {}'.format(ciphertext))
    
    plaintext = des.decryption(ciphertext, key2)
    # plaintext = des.decryption(ciphertext, key2, mod='CBC', iv=IV)
    with open('plaintext.txt', 'w+') as f:
        f.write('{}\n'.format(plaintext))
    print('明文: {}'.format(plaintext))
