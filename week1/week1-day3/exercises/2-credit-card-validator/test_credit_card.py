import unittest


from credit_card import CreditCard


#do not modify assert statements
class TestCreditCard(unittest.TestCase):
	def test_credit_card_9999999999999999(self):
		cc = CreditCard('9999999999999999')
		
		self.assertFalse(cc.valid, msg="Credit Card number cannot start with 9")
		self.assertEqual(cc.card_type, "INVALID", msg="99... card type is 'INVALID'")

	def test_credit_card_4440(self):
		cc = CreditCard('4440')

		self.assertFalse(cc.valid, msg="4440 is too short to be valid")
		self.assertEqual(cc.card_type, "INVALID", msg="4440 card type should be INVALID")

	def test_credit_card_5515460934365316(self):
		cc = CreditCard('5515460934365316')

		self.assertTrue(cc.valid, msg="Mastercard is Valid")
		self.assertEqual(cc.card_type, "MASTERCARD", msg="card_type is MASTERCARD")

	def test_credit_card_6011053711075799(self):
		cc = CreditCard('6011053711075799')

		self.assertTrue(cc.valid, msg="Discover Card is Valid")
		self.assertEqual(cc.card_type, "DISCOVER", msg="card_type is DISCOVER")

	def test_credit_card_379179199857686(self):
		cc = CreditCard('379179199857686')

		self.assertTrue(cc.valid, msg="AMEX is Valid")
		self.assertEqual(cc.card_type, "AMEX", msg="card_type is AMEX")

	def test_credit_card_4929896355493470(self):
		cc = CreditCard('4929896355493470')

		self.assertTrue(cc.valid, msg="Visa Card is Valid")
		self.assertEqual(cc.card_type, "VISA", msg="card_type is VISA")

	def test_credit_card_4329876355493470(self):
		cc = CreditCard('4329876355493470')

		self.assertFalse(cc.valid, msg="This card does not meet mod10")
		self.assertEqual(cc.card_type, "INVALID", msg="card_type should be INVALID")

	def test_credit_card_339179199857685(self):
		cc = CreditCard('339179199857685')

		self.assertFalse(cc.valid, msg="Validates mod10, but invalid starting numbers for AMEX")
		self.assertEqual(cc.card_type, "INVALID", msg="card_type should be INVALID")