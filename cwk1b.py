def ext_vigenere(text, key):
    key = list(key)
    if len(text) == len(key):
        return(key)
    else:
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return ("" .join(key))

def encrypt(text, key):
    encrypt_text = []
    for i in range(len(text)):
        x = (ord(text[i]) + ord(key[i])) % 26
        x += ord ('A')
        encrypt_text.append(chr(x))
    return ("".join(encrypt_text))

def decrypt(text, key):
    original_text = []
    for i in range(len(text)):
        x = (ord(text[i]) - ord(key[i]) + 26) % 26
        x += ord ('A')
        original_text.append(chr(x))
    return ("".join(original_text))


if __name__ == "__main__":
    string = "VIGENERE"
    keyword = "CIPHERCI"
    key = ext_vigenere(string, keyword)
    encrypt_text = encrypt(string, key)
    # print(encrypt_text)
    # print (decrypt(encrypt_text, key))