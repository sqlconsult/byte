#!/usr/bin/env python3


class VigenereCipher:
    def __init__(self, keyword):
        self.keyword = keyword

    def combine_character(self, plain, keyword):
        """
        Convert plain text and keyword characters to their
        numerical values, add them together and take the
        remainder mod 26 to get the cipher text character
        :param plain: Plain text character
        :param keyword: keyword for encryption
        :return: plain text mapped to cipher character using keyword
        """
        #

        #
        plain = plain.upper()
        keyword = keyword.upper()
        plain_num = ord(plain) - ord('A')
        keyword_num = ord(keyword) - ord('A')
        ret_char = chr(ord('A') + (plain_num + keyword_num) % 26)
        return ret_char

    def extend_keyword(self, number):
        """
        Extend the cipher keyword to a specified number of characters
        :param number: How long to make the keyword
        :return: keyword copied as many times as necessary to make it
                 length = specified number of characters
        """
        #  “floor” division (rounds down to nearest whole number)
        repeats = number // len(self.keyword) + 1
        ret_str = (self.keyword * repeats) [:number]
        return ret_str

    def separate_character(self, cypher, keyword):
        """
        Decode a single character using keyword
        :param cypher: Chracter to decode
        :param keyword: keyword to use
        :return: Decoded character
        """
        cypher = cypher.upper()
        keyword = keyword.upper()
        cypher_num = ord(cypher) - ord('A')
        keyword_num = ord(keyword) - ord('A')
        ret_char = chr(ord('A') + (cypher_num - keyword_num) % 26)
        return ret_char

    def _code(self, text, combine_func):
        """
        Encode plain text or decode encrypted text using combine_func
        :param text:
        :param combine_func:
        :return:
        """
        # remove spaces & make all uppercase
        text = text.replace(' ', '').upper()

        # initialize return list
        combined = []

        # extend keyword to be same length as plain text
        keyword = self.extend_keyword(len(text))

        # The purpose of zip() is to map the similar index of multiple containers
        # so that they can be used just using as single entity.
        for p, k in zip(text, keyword):
            combined.append(combine_func(p,k))
        return ''.join(combined)

    def encode(self, plaintext):
        """
        Encodes plain text and returns encoded text
        :param plaintext: Text to encode
        :return: Encrypted text
        """
        return self._code(plaintext, self.combine_character)

    def decode(self, ciphertext):
        """
        Decodes encoded text and returns plain text
        :param ciphertext: Text to decode
        :return: Plain text
        """
        return self._code(ciphertext, self.separate_character)
