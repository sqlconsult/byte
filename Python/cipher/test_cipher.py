#!/usr/bin/env python3

import cipher as c


class TestCipher:

    def setup(self):
        """
        run at beginning of module of test code
        :return:
        """
        print("setup             class: TestCipher")

    def teardown(self):
        """
        Run at end of module of test code
        :return:
        """
        print("teardown          class: TestCipher")

    def setup_class(cls):
        """
        Run at beginning of class of test methods
        :return:
        """
        print("setup_class       class:%s" % cls.__name__)

    def teardown_class(cls):
        """
        Run at end of class of test methods
        :return:
        """
        print("teardown_class    class:%s" % cls.__name__)

    def setup_method(self, method):
        """
        Run before a test method call
        :param method:
        :return:
        """
        print("setup_method      method:%s" % method.__name__)

    def teardown_method(self, method):
        """
        Run after a test method call
        :param method:
        :return:
        """
        print("teardown_method   method:%s" % method.__name__)

    def test_encode(self):
        cipher_obj = c.VigenereCipher('TRAIN')
        encoded = cipher_obj.encode('ENCODEDINPYTHON')
        assert encoded == 'XECWQXUIVCRKHWA'

    def test_encode_character(self):
        cipher_obj = c.VigenereCipher('TRAIN')
        encoded = cipher_obj.encode('E')
        assert encoded == 'X'

    def test_encode_spaces(self):
        cipher_obj = c.VigenereCipher('TRAIN')
        encoded = cipher_obj.encode('ENCODED IN PYTHON')
        assert encoded == 'XECWQXUIVCRKHWA'

    def test_encode_lowercase(self):
        cipher_obj = c.VigenereCipher('TRain')
        encoded = cipher_obj.encode('encoded in Python')
        assert encoded == 'XECWQXUIVCRKHWA'

    def test_combine_character(self):
        cipher_obj = c.VigenereCipher('TRain')
        assert cipher_obj.combine_character('E', 'T') == 'X'
        assert cipher_obj.combine_character('N', 'R') == 'E'

    def test_extend_keyword(self):
        cipher_obj = c.VigenereCipher('TRAIN')
        extended = cipher_obj.extend_keyword(16)
        assert extended == 'TRAINTRAINTRAINT'

    def test_decode_character(self):
        cipher_obj = c.VigenereCipher('TRAIN')
        encoded = cipher_obj.decode('X')
        assert encoded == 'E'

    def test_decode(self):
        cipher_obj = c.VigenereCipher('TRAIN')
        encoded = cipher_obj.decode('XECWQXUIVCRKHWA')
        assert encoded == 'ENCODEDINPYTHON'
