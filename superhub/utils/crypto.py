import base64


def encode(key, plaintext):
    ciphertext = []
    for i in range(len(plaintext)):
        key_c = key[i % len(key)]
        enc_c = (ord(plaintext[i]) + ord(key_c)) % 256
        ciphertext.append(enc_c)
    return base64.urlsafe_b64encode(bytes(ciphertext))


def decode(key, ciphertext):
    plaintext = []
    ciphertext = base64.urlsafe_b64decode(ciphertext)
    for i in range(len(ciphertext)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ciphertext[i] - ord(key_c)) % 256)
        plaintext.append(dec_c)
    return "".join(plaintext)


if __name__ == "__main__":
    key = "6a5s4d6%^$^SA^%"
    plaintext = "The brown lazy fox jumped over the fence."
    ciphertext = encode(key, plaintext)
    print(ciphertext)
    print(decode(key, ciphertext))
