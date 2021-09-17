class Atm:
    def __init__(self,cardNumber,pin):
        self.cardNumber=cardNumber
        self.pin=pin
    def checkbalance(self):
        print("Your Balance Is 500")
    def withdraw(self,amount):
        newAmount=500-amount
        print(newAmount)
        

atm1=Atm(20,30) 
atm1.checkbalance() 
atm1.withdraw(40)

