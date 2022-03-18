
import string
import random
from collections import Counter


class SimpleReplacementEncrypter:

    def __init__(self, alphabet:str = string.ascii_letters, key:str = None) -> None:

        if is_set_of_chars(alphabet):
            self._alphabet = alphabet
        else:
            raise ValueError("Wrong alphabet")

        if self.check_key_correctness(key):
            self._key = key
        else:
            self._key = None

        if self._key == None:
            self.generate_key()

    
    @property
    def key(self):
        return self._key


    def generate_key(self):
        self._key = "".join(random.sample(self._alphabet,len(self._alphabet)))


    def check_key_correctness(self, key:str):
        if isinstance(key,str):
            if len(key) == len(self._alphabet):
                if is_set_of_chars(key):
                    return True
            return False


    def encrypt(self, message: str):
        if self.check_key_correctness(self._key):
            result = ""
            for i in range(len(message)):
                if message[i] in self._alphabet:
                    result+= self._key[ self._alphabet.find(message[i])]
                else:
                    result+= message[i]
            return result
        else:
            return None


    def decrypt(self, encrypted_message: str):
        if self.check_key_correctness(self._key):
            result = ""
            for i in range(len(encrypted_message)):
                if encrypted_message[i] in self._key:
                    result+= self._alphabet[ self._key.find(encrypted_message[i])]
                else:
                    result+= encrypted_message[i]
            return result
        else:
            return None



def is_set_of_chars(text:str) -> bool:
    if isinstance(text, str):
        frequency_counter = Counter(text)
        if len(frequency_counter) == len(text):
            return True
    
    return False


def main():
    
    message = "I like kitkat"

    encrypter = SimpleReplacementEncrypter()
    encrypter.generate_key()

    encrypted = encrypter.encrypt(message)
    print(encrypted)
    print(encrypter.decrypt(encrypted))
    


if __name__ == "__main__":
    main()
