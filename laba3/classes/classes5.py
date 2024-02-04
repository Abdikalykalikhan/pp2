class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance            

        
    def deposit(self, money):
        self.balance = self.balance + money
        print(f"Your balance : {self.balance}")

        
    def withdraw(self, money):
        if self.balance < money:
            print("Lack of money!")
            print(f"Your balance : {self.balance}")
        else:
            self.balance = self.balance - money
            print(f"Your balance : {self.balance}")
 
p1 = Account("Alikhan Abdikalyk", balance = 0)

p1.deposit(1000)
p1.withdraw(1000)
p1.withdraw(100)
p1.deposit(1000000)