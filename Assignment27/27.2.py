class BankAccount:

    ROI = 10.5

    # Constructor
    def __init__(self, name ,amount ):

        #Instance Variables as in init method
        self.Name = name
        self.Amount = amount

    def Display(self):
        print("Account Holder :", self.Name)
        print("Current Balance :", self.Amount)

    def Deposit(self):
        Deposited_amt = int(input("Enter Deposit Amount : "))
        self.Amount = self.Amount + Deposited_amt
        print("Amount Deposited Successfully.")

    def Withdraw(self):
        Withdrawal_amt = int(input("Enter Withdraw Amount : "))

        if self.Amount >= Withdrawal_amt:
            self.Amount = self.Amount - Withdrawal_amt
            print("Withdrawal Successful.")
        else:
            print("Insufficient Balance!")
        
    def CalculateInterest(self):
        Interest = ( self.Amount * BankAccount.ROI ) / 100
        return Interest

def main():

    Obj1 = BankAccount("ABC",11000)
    Obj2 = BankAccount("PQR",21000)

    Obj1.Display()
    Obj1.Deposit()
    Obj1.Withdraw()
    print("Interest :", Obj1.CalculateInterest())

    Obj2.Display()
    Obj2.Deposit()
    Obj2.Withdraw()
    print("Interest :", Obj2.CalculateInterest())
    
if __name__ == "__main__":
    main()
