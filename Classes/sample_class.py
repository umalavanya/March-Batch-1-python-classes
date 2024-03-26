class Account():
    num_accounts = 0 
    def __init__(self,name, balance ):
        self.name = name
        self.balance = balance
        Account.num_accounts += 1
        
    def __deleting__():
        Account.num_accounts -= 1
        
    def deposit(self, amount):
        self.balance = self.balance + amount
        
    def withdraw(self, amount):
        self.balance = self.balance - amount
        if self.balance == 0 :
            self.deleting()
            
        
    def inquiry(self):
        return self.balance
        
