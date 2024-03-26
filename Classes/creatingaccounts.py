import sample_class as ac 

account1 = ac.Account("Iyyappan", 500)

print(account1.name, account1.inquiry())
account1.deposit(1000)
print(account1.inquiry())

account2 = ac.Account("Madhu", 500)
print(account2.inquiry())

account1.withdraw(200)
print(account1.inquiry())
