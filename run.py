import des

if __name__ == '__main__':
    mes = "abcd1234abcd1234"
    IV = 'abcd1234'    #初始向量
    key = 'abcd1234'   #密钥
    print('----------------------------------------------------------------------')
    print('----------------------------------------------------------------------')
    print('消息: {}'.format(mes))
    print('----------------------------------------------------------------------')
    print('----------------------------------------------------------------------')
    ciphertext = des.encryption(mes, key)
    # ciphertext = des.encryption(mes, key, mod='CBC', iv=IV)
    with open('ciphertext.txt', 'w+', encoding='utf-8') as f:
        f.write('{}\n'.format(ciphertext))
    print('加密: {}'.format(ciphertext))
    print('----------------------------------------------------------------------')
    print('----------------------------------------------------------------------')
    plaintext = des.decryption(ciphertext, key)
    # plaintext = des.decryption(ciphertext, key, mod='CBC', iv=IV)
    with open('plaintext.txt', 'w+') as f:
        f.write('{}\n'.format(plaintext))
    print('解密: {}'.format(plaintext))
    print('----------------------------------------------------------------------')
    print('----------------------------------------------------------------------')
