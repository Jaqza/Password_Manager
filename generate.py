import random
CAPITAL_LETTERS = 1
LETTERS = 5
SPECIAL_SIGN = 1
NUMBERS = 2

class Generator:
    def __init__(self):
        self.numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.signs = ["!","@","#","$","%","^","&","*","(",")"]
        self.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.upper_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.password_list = []

    def password_elements(self,prime_list, signs_quantity):
        """Inner funktion of password generator , do not use it"""
        for choice in range(0,signs_quantity):
            sign = random.choice(prime_list)
            self.password_list.append(sign)

    def generate_new_password(self):
        """Return random password as string"""
        self.password_list.clear()
        self.password_elements(self.upper_alphabet, CAPITAL_LETTERS)
        self.password_elements( self.alphabet, LETTERS)
        self.password_elements( self.signs, SPECIAL_SIGN)
        self.password_elements(self.numbers, NUMBERS)
        random.shuffle(self.password_list)
        new_password = "".join(self.password_list)
        return new_password




