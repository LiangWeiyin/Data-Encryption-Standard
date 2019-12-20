import des

if __name__ == '__main__':
    mes = "Hello World!"
    IV = list('0110000101100010011000110110010000110001001100100011001100110100')    #abcd1234
    key1 = list('0110000101100010011000110110010000110001001100100011001100110100')  #abcd1234
    key2 = list('0110000101100010011000110110010000110001001100100011001100110100')  #abcd1234
    print('----------------------------------------------------------------------')
    print('----------------------------------------------------------------------')
    print('消息: {}'.format(mes))
    print('----------------------------------------------------------------------')
    print('----------------------------------------------------------------------')
    ciphertext = des.encryption(mes, key1)
    # ciphertext = des.encryption(mes, key1, mod='CBC', iv=IV)
    with open('ciphertext.txt', 'w+', encoding='utf-8') as f:
        f.write('{}\n'.format(ciphertext))
    print('加密: {}'.format(ciphertext))
    print('----------------------------------------------------------------------')
    print('----------------------------------------------------------------------')
    plaintext = des.decryption(ciphertext, key2)
    # plaintext = des.decryption(ciphertext, key2, mod='CBC', iv=IV)
    with open('plaintext.txt', 'w+') as f:
        f.write('{}\n'.format(plaintext))
    print('解密: {}'.format(plaintext))
    print('----------------------------------------------------------------------')
    print('----------------------------------------------------------------------')
