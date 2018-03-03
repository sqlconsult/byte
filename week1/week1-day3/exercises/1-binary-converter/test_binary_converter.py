import unittest


from binary_converter import binary_to_decimal, decimal_to_binary


#do not modify these statements
class TestBinaryToDecimal(unittest.TestCase):
	def test_binary_to_decimal_0(self):
		self.assertEqual(binary_to_decimal(0), 0, msg="0 to decimal should return 0")

	def test_binary_to_decimal_1011(self):
		self.assertEqual(binary_to_decimal(1011), 11, msg="1011 to decimal should return 11")

	def test_binary_to_decimal_101011(self):
		self.assertEqual(binary_to_decimal(101011), 43, msg="101011 to decimal should return 43")

	def test_binary_to_decimal_101011101(self):
		self.assertEqual(binary_to_decimal(101011101), 349, msg="101011101 to decimal should return 349")


class TestDecimalToBinary(unittest.TestCase):
	def test_decimal_to_binary_0(self):
		self.assertEqual(decimal_to_binary(0), 0, msg="0 to binary should return 0")
	
	def test_decimal_to_binary_5(self):
		self.assertEqual(decimal_to_binary(5), 101, msg="5 to binary should return 101")

	def test_decimal_to_binary_10(self):
		self.assertEqual(decimal_to_binary(10), 1010, msg="10 to binary should return 1010")

	def test_decimal_to_binary_113(self):
		self.assertEqual(decimal_to_binary(113), 1110001, msg="113 to binary should return 1110001")
