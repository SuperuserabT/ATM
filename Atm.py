class Atm:
    def __init__(self, cardNumber, pinNumber, balance):
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber
        self.balance = balance

    def balanceEnquiry(self):
        print(self.balance)

    def cashWithdrawal(self, amount):
        self.balance = self.balance - amount

user = Atm(326, 5529, 250000)