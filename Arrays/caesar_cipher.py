"""python example playing with Arrays to make a cipher"""

class CaesarCipher:
    """
    decryption and encryption using a Caeser cipher
    only works for CAPS messages right now
    """
    def __init__(self, shift):
        encoder = [None] * 26
        decoder = [None] * 26
        for index in range(26):
            encoder[index] = chr((index + shift) % 26 + ord('A'))
            decoder[index] = chr((index - shift) % 26 + ord('A'))
        self.forward = ''.join(encoder)
        self.backward = ''.join(decoder)

    def encrypt(self, message):
        """
        encrypt message with cipher
        """
        return self.transform(message, self.forward)

    def decrypt(self, secret):
        """
        decrypt message with cipher
        """
        return self.transform(secret, self.backward)

    def transform(self, original, code):
        """
        transform message with cipher O(n)
        """
        message = list(original)
        for index in range(len(message)):
            if message[index].isupper():
                x = ord(message[index]) - ord('A')
                message[index] = code[x]
        return ''.join(message)
