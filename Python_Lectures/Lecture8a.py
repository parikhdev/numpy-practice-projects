# Create a Class of Bank details having Account Number, Balance as Attributes.
# Create the Debit and Credit methods to update the Balance.

class Bank_Details:
    def __init__(self, Balance, Account_Number):
        self.Balance = Balance
        self.Account_Number = Account_Number

    def Credit(self, amount):
        self.Balance += amount
        print("Your Account is Credited with", amount, ", New Balance is", self.Total_Balance())

    def Debit(self, amount):
        self.Balance -= amount
        print("Your Account is Debited with", amount, ", New Balance is", self.Total_Balance())

    def Total_Balance(self):
        return self.Balance

account1 = Bank_Details(1000, "123456789")
account1.Credit(700)
account1.Debit(200)
account1.Total_Balance()