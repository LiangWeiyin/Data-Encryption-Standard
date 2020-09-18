import des

if __name__ == '__main__':
    mes = "革命尚未成功, 同志仍需努力"
    IV = 'abcd1234'    # 初始向量 CBC 模式
    key = 'abcd1234'   # 密钥

    print()
    print('消息: {}'.format(mes))
    # ciphertext = des.encryption(mes, key)
    ciphertext = des.encryption(mes, key, mod='CBC', iv=IV)
    # with open('ciphertext.txt', 'w+', encoding='utf-8') as f:
    #     f.write('{}\n'.format(ciphertext))
    print()
    print('加密: {}'.format(ciphertext))
    # plaintext = des.decryption(ciphertext, key)
    plaintext = des.decryption(ciphertext, key, mod='CBC', iv=IV)
    # with open('plaintext.txt', 'w+', encoding="utf-8") as f:
    #     f.write('{}\n'.format(plaintext))
    print()
    print('解密: {}'.format(plaintext))
    print()