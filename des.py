import random
import string
from var import *


def string_to_bits(data, type):
    # 字符串 --> 01串
    """
    type: 1 加密
    type: 0 解密
    """
    if type == 1:
        bytes_list = list(bytes(data, encoding='utf-8'))
        res = list(''.join(bin(x)[2:].zfill(8) for x in bytes_list))
        temp = len(res) % 64
        if temp != 0:  # 不够64bit,补0.
            for _ in range(64 - temp):
                res.append('0')
        return res

    elif type == 0:
        char_list = list(data)
        temp = [bin(int(x, 16))[2:].zfill(4) for x in char_list]
        res = ''.join(temp)
        return res


def bits_to_string(data, type):
    # 01串 --> 16 进制字符串
    """
    type: 1 加密
    type: 0 解密
    """
    if type == 1:
        temp = [hex(int(''.join(data[ind:ind+4]), 2))[2:]
                for ind in range(0, len(data), 4)]
        res = ''.join(temp)
        return res
    elif type == 0:
        while (''.join(data[-8:]) == '00000000'):
            data = data[:-8]
        temp = [int(''.join(data[ind:ind+8]), 2)
                for ind in range(0, len(data), 8)]
        res = bytes(temp).decode('utf-8')
        return res


def text_slice(text):
    # 明文分组
    return [text[ind:ind+64] for ind in range(0, len(text), 64)]


def permutation(data, matrix):
    # 矩阵置换
    res = []
    for val in matrix:
        res.append(data[val-1])
    return res


def gen_key():
    # 生成64bit秘钥
    return random.choices('01', k=64)


def gen_subkeys(key):
    # 生成16个子秘钥
    sub_keys = []
    permu_key = permutation(key, PERMUTED_CHOICE_1)
    left_block = permu_key[:28]
    right_block = permu_key[28:]
    for i in range(16):
        temp_left = left_shift(left_block, KEY_SHIFT_AMOUNTS[i])
        temp_right = left_shift(right_block, KEY_SHIFT_AMOUNTS[i])
        sub_key = permutation(temp_left+temp_right, PERMUTED_CHOICE_2)
        sub_keys.append(sub_key)
        left_block, right_block = temp_left, temp_right
    return sub_keys


def left_shift(s, num):
    # 循环左移
    return s[num:] + s[:num]


def xor(s1, s2):
    # 异或
    res = []
    for i in zip(s1, s2):
        if i[0] == i[1]:
            res.append('0')
        else:
            res.append('1')
    return res


def F_fuction(right_bolck, subkey):
    # 轮函数, S-BOX变换
    res = []
    expand_right = permutation(right_bolck, EXPANSION)
    right_xor_key = xor(expand_right, subkey)
    data_for_sbox = [right_xor_key[ind:ind+6]
                     for ind in range(0, len(right_xor_key), 6)]
    for ind, val in enumerate(data_for_sbox):
        s_row = int(''.join([val[0], val[-1]]), 2)
        s_column = int(''.join(val[1:-1]), 2)
        temp = list(bin(SBOXES[ind][s_row][s_column])[2:].zfill(4))
        res.extend(temp)
    return permutation(res, PERMUTATION)


def round(subkeys, block):
    # 16次轮变换
    left_block, right_block = block[:32], block[32:]
    for ind in range(16):
        temp = right_block
        sbox_out = F_fuction(right_block, subkeys[ind])
        right_block = xor(left_block, sbox_out)
        left_block = temp
    return right_block + left_block


def encryption(text, key, mod='ECB', iv=''):
    # 加密
    res = []
    bits = string_to_bits(text, type=1)
    group_text = text_slice(bits)
    k = string_to_bits(key, type=1)
    subkeys = gen_subkeys(k)
    if mod == 'ECB':
        for block in group_text:
            permu_text = permutation(block, INITIAL_PERMUTATION)
            round_end = round(subkeys, permu_text)
            final_permu_text = permutation(round_end, FINAL_PERMUTATION)
            res.extend(final_permu_text)
        ciphertext = bits_to_string(res, type=1)
        return ciphertext
    elif mod == 'CBC':
        IV = string_to_bits(iv, type=1)
        for block in group_text:
            xor_block = xor(block, IV)
            permu_text = permutation(xor_block, INITIAL_PERMUTATION)
            round_end = round(subkeys, permu_text)
            final_permu_text = permutation(round_end, FINAL_PERMUTATION)
            res.extend(final_permu_text)
            IV = final_permu_text
        ciphertext = bits_to_string(res, type=1)
        return ciphertext


def decryption(text, key, mod='ECB', iv=''):
    # 解密
    res = []
    bits = string_to_bits(text, type=0)
    group_text = text_slice(bits)
    k = string_to_bits(key, type=1)
    subkeys = gen_subkeys(k)
    subkeys.reverse()  # 调换子密钥顺序
    if mod == 'ECB':
        for block in group_text:
            permu_text = permutation(block, INITIAL_PERMUTATION)
            round_end = round(subkeys, permu_text)
            final_permu_text = permutation(round_end, FINAL_PERMUTATION)
            res.extend(final_permu_text)
        plaintext = bits_to_string(res, type=0)
        return plaintext
    if mod == 'CBC':
        IV = string_to_bits(iv, type=1)
        for block in group_text:
            permu_text = permutation(block, INITIAL_PERMUTATION)
            round_end = round(subkeys, permu_text)
            final_permu_text = permutation(round_end, FINAL_PERMUTATION)
            xor_block = xor(final_permu_text, IV)
            res.extend(xor_block)
            IV = block
        plaintext = bits_to_string(res, type=0)
        return plaintext
