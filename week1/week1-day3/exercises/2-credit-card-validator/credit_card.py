class CreditCard:

    def __init__(self, card_number):
        self.card_number = card_number
        self.card_type = "INVALID"
        self.valid = False

        self.validate()


    def determine_card_type(self):
        card_type = 'INVALID'

        valid_mastercard = [ '51', '52', '53', '54', '55' ]

        if str(self.card_number)[0] == '4':
            # print (Visa)
            card_type = 'VISA'
        elif str(self.card_number)[0:2] in valid_mastercard:
            # print(Mastercard)
            card_type = 'MASTERCARD'
        elif str(self.card_number)[0:2] in ['34', '37']:
            # print(AMEX)
            card_type = 'AMEX'
        elif str(self.card_number)[0:4] == '6011':
            # print (Discover)
            card_type = 'DISCOVER'

        return card_type


    def check_length(self):
        valid_len = False
        card_type = self.determine_card_type()
        if len(self.card_number) == 16 and card_type in ['VISA', 'MASTERCARD', 'DISCOVER' ]:
            # print("Visa,Mastercard,Discover")
            valid_len = True
        elif len (self.card_number) == 15 and card_type == 'AMEX':
            # print("AMEX")
            valid_len = True

        return valid_len


    def  check_luhn(self):
        result = False

        c = self.card_number

        # digits to add as is start at -1 and skip every other character
        digits = list(c[-1::-2])

        # digits to double start at -2 and skip every other character
        digits_to_double = list(c[-2::-2])

        # compute sum
        sum = 0

        # add individual even position digits to sum
        for i in digits:
            sum += int(i)

        # double odd position digits and add individual double digit value to sum
        # for example: if digit == 4 --> add 8 to sum
        #              if digit == 8 --> add 1 + 6 (7) to sum
        for i in digits_to_double:
            double = int(i) * 2
            if len(str(double)) > 1:
                s1 = str(double)
                d1 = s1[0]
                d2 = s1[1]
                sum += int(d1) + int(d2)
            else:
                sum += double
 
        # if sum is multiple of 10, then this is a valid card number
        if sum % 10 == 0:
            result = True

        return result



    def validate(self):
        """
        Create and add your method called 'validate' to the CreditCard class here:
        """

        self.card_type = 'INVALID'
        self.valid = False

        card_type = self.determine_card_type()

        if self.check_length() and self.check_luhn():
            self.card_type = card_type
            self.valid = True


def main():
    """
    Write your custom tests here
    """
#    print('===== Start =====')
#    cc = CreditCard('9999999999999999')    # 1 - Invalid - card type
#    print('1 - Credit Card Number: ', cc.card_number, 'Card Type: ', cc.card_type, 'Valid: ', cc.valid)

#    cc = CreditCard('4440')                # 2 - Invalid - too short
#    print('2 - Credit Card Number: ', cc.card_number, 'Card Type: ', cc.card_type, 'Valid: ', cc.valid)

#    cc = CreditCard('5515460934365316')    # 3 - Mastercard - Valid
#    print('3 - Credit Card Number: ', cc.card_number, 'Card Type: ', cc.card_type, 'Valid: ', cc.valid)

#    cc = CreditCard('6011053711075799')    # 4 - Discover - Valid
#    print('4 - Credit Card Number: ', cc.card_number, 'Card Type: ', cc.card_type, 'Valid: ', cc.valid)

#    cc = CreditCard('379179199857686')     # 5 - Amex - Valid
#    print('5 - Credit Card Number: ', cc.card_number, 'Card Type: ', cc.card_type, 'Valid: ', cc.valid)

#    cc = CreditCard('4929896355493470')    # 6 - Visa - valid
#    print('6 - Credit Card Number: ', cc.card_number, 'Card Type: ', cc.card_type, 'Valid: ', cc.valid)

#    cc = CreditCard('4329876355493470')    # 7 - Visa - Invalid - mod 10
#    print('7 - Credit Card Number: ', cc.card_number, 'Card Type: ', cc.card_type, 'Valid: ', cc.valid)

#    cc = CreditCard('339179199857685')     # 8 - Amex - Invalid - starting numbers
#    print('8 - Credit Card Number: ', cc.card_number, 'Card Type: ', cc.card_type, 'Valid: ', cc.valid)

#    print('===== Done  =====')
    pass


if __name__ == '__main__':
    main()
